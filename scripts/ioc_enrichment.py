#!/usr/bin/env python3
"""
  python3 ioc_enrichment.py --input iocs.txt
"""

import argparse
import ipaddress

def parse_args():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True, help="File with one IP per line")
    return ap.parse_args()

def classify(ip: str) -> str:
    try:
        addr = ipaddress.ip_address(ip)
    except ValueError:
        return "INVALID"
    if addr.is_private:
        return "PRIVATE_RFC1918"
    if addr.is_loopback:
        return "LOOPBACK"
    if addr.is_multicast:
        return "MULTICAST"
    if addr.is_reserved:
        return "RESERVED"
    return "PUBLIC"

def main():
    args = parse_args()
    with open(args.input, "r", encoding="utf-8") as f:
        for line in f:
            ip = line.strip()
            if not ip:
                continue
            print(f"{ip}\t{classify(ip)}\tnote=review_in_siem")

if __name__ == "__main__":
    main()
