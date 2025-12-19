# Portfolio Case Study: Enterprise Security Lab Environment

## Problem
I needed a realistic environment to practice and demonstrate enterprise security skills beyond isolated tools. I built a lab that shows network segmentation, identity centralization, monitoring, detection engineering, and incident response validation.

## Goal
- Build a segmented enterprise network with centralized identity.
- Collect endpoint + network telemetry into a SIEM.
- Detect real attack behaviors (not just signatures). 
- Validate detections through controlled offensive testing.
- Produce documentation and artifacts that are interview-ready.

## Architecture
- VirtualBox hosts pfSense, Windows Server (AD), Windows clients, Kali, SIEM, and IDS tooling.
- VLANs separate domain services, users, security tooling, and management.
- pfSense routes between VLANs and enforces least privilege.
- Sysmon + Windows event logs feed SIEM.
- Suricata inspects mirrored traffic for network indicators.

## What I Implemented
- VLAN segmentation and inter-VLAN firewall rules.
- Active Directory domain, OUs, accounts, and Group Policy.
- Endpoint logging (Windows Security logs + Sysmon).
- Splunk and ELK ingestion pipelines.
- Suricata IDS ruleset and alerting.
- Dashboards for failed logons, lateral movement indicators, and beaconing.
- Automation scripts for scanning, beacon detection, and IOC enrichment.
- Attack simulations and response playbooks.

## Scenarios Tested (Examples)
1) Password spraying against domain users
2) SMB-based lateral movement attempt
3) Web app attack workflow via Burp Suite (targeted lab service)
4) C2 beacon simulation and detection via periodic callbacks

Each scenario is documented with:
- Attack steps and commands
- Expected telemetry (Windows + network)
- SIEM detection logic (queries + thresholds)
- Response actions (containment + evidence collection)

## Results / Evidence
- Created repeatable detections that correlate endpoint + network signals.
- Validated detections by reproducing attacker behaviors and confirming SIEM alerts.
- Produced a structured repo with configs, scripts, dashboards, and incident walkthroughs.

## Skills Demonstrated
Network security engineering, Active Directory + IAM, SIEM operations, IDS tuning, detection engineering, incident response, automation (Python/Bash/PowerShell), and governance mapping (NIST 800-53).

## Next Improvements
- Add Sigma rules + automatic conversion to Splunk queries
- Integrate Azure Log Analytics/Sentinel for hybrid correlation
- Add atomic testing for common ATT&CK techniques
