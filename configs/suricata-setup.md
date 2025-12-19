# Suricata Setup 

## Mode
- IDS mode recommended for lab validation

## Inputs
- Monitor pfSense LAN/VLAN trunk interface 

## Rules
- Emerging Threats community rules
- Local rules for:
  - Port scan patterns
  - SMB brute-force indicators
  - Suspicious DNS patterns
  - Beacon-like periodic callbacks

## Output
- EVE JSON for ingestion into ELK or Splunk
