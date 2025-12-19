#!/usr/bin/env python3
"""
  python3 beacon_detector.py --input eve.json --min-events 20 --max-jitter-sec 3
"""

import argparse
import json
from collections import defaultdict
from datetime import datetime

def parse_args():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--min-events", type=int, default=20)
    ap.add_argument("--max-jitter-sec", type=float, default=3.0)
    return ap.parse_args()

def parse_ts(ts: str) -> datetime:
    # Suricata timestamps often look like: 2025-12-19T12:34:56.123456+0000
    ts = ts.replace("Z", "+0000")
    for fmt in ("%Y-%m-%dT%H:%M:%S.%f%z", "%Y-%m-%dT%H:%M:%S%z"):
        try:
            return datetime.strptime(ts, fmt)
        except ValueError:
            continue
    raise ValueError(ts)

def main():
    args = parse_args()
    flows = defaultdict(list)

    with open(args.input, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue

            # best-effort field mapping
            src = obj.get("src_ip") or obj.get("source_ip")
            dst = obj.get("dest_ip") or obj.get("destination_ip")
            dport = obj.get("dest_port") or obj.get("destination_port")
            ts = obj.get("timestamp") or obj.get("time")
            if not (src and dst and dport and ts):
                continue

            try:
                t = parse_ts(ts)
            except Exception:
                continue

            flows[(src, dst, int(dport))].append(t)

    for (src, dst, dport), times in flows.items():
        if len(times) < args.min_events:
            continue
        times.sort()
        deltas = [(times[i] - times[i-1]).total_seconds() for i in range(1, len(times))]
        if not deltas:
            continue
        avg = sum(deltas) / len(deltas)
        max_dev = max(abs(d - avg) for d in deltas)

        if max_dev <= args.max_jitter_sec and avg > 5:
            print(f"[BEACON] {src} -> {dst}:{dport} events={len(times)} avg_interval={avg:.2f}s max_jitter={max_dev:.2f}s")

if __name__ == "__main__":
    main()
