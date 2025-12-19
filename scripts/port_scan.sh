#!/usr/bin/env bash
# Simple controlled scanner run from Kali.
# Usage: ./port_scan.sh 10.10.20.0/24

set -euo pipefail

TARGET="${1:-}"
if [[ -z "$TARGET" ]]; then
  echo "Usage: $0 <target IP or CIDR>"
  exit 1
fi

OUTDIR="outputs"
mkdir -p "$OUTDIR"
TS="$(date +%Y%m%d_%H%M%S)"
OUTFILE="$OUTDIR/nmap_${TS}.txt"

echo "[*] Scanning: $TARGET"
nmap -sS -sV -T3 --reason --open "$TARGET" | tee "$OUTFILE"
echo "[+] Saved: $OUTFILE"
