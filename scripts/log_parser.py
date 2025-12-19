#!/usr/bin/env python3
"""
Parse Windows Security log exports (CSV) to find failed logon bursts.
Input CSV expected columns: TimeCreated, EventID, TargetUser, SourceIP
Usage:
  python3 log_parser.py --input security_events.csv --window-min 5 --threshold 10
"""

import argparse
import csv
from collections import defaultdict
from datetime import datetime, timedelta

def parse_args():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True, help="CSV file of events")
    ap.add_argument("--window-min", type=int, default=5, help="Window size in minutes")
    ap.add_argument("--threshold", type=int, default=10, help="Alert threshold per user/IP per window")
    return ap.parse_args()

def parse_time(s: str) -> datetime:
    
    for fmt in ("%Y-%m-%d %H:%M:%S", "%m/%d/%Y %H:%M:%S", "%Y-%m-%dT%H:%M:%S"):
        try:
            return datetime.strptime(s, fmt)
        except ValueError:
            continue
    raise ValueError(f"Unrecognized time format: {s}")

def main():
    args = parse_args()
    window = timedelta(minutes=args.window_min)

    events = []
    with open(args.input, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            try:
                t = parse_time(row["TimeCreated"])
            except Exception:
                continue
            events.append((t, row.get("EventID",""), row.get("TargetUser",""), row.get("SourceIP","")))

    events.sort(key=lambda x: x[0])
    buckets = defaultdict(int)

    start_idx = 0
    for i in range(len(events)):
        t, _, user, ip = events[i]
        while events[start_idx][0] < t - window:
            old_t, _, old_user, old_ip = events[start_idx]
            buckets[(old_user, old_ip, old_t.replace(second=0, microsecond=0))] -= 1
            start_idx += 1

        key = (user, ip, (t - timedelta(minutes=t.minute % args.window_min)).replace(second=0, microsecond=0))
        buckets[key] += 1

        if buckets[key] == args.threshold:
            u, s_ip, bucket_time = key
            print(f"[ALERT] Failed-logon burst: user={u} source_ip={s_ip} window_start={bucket_time} count>={args.threshold}")

if __name__ == "__main__":
    main()
