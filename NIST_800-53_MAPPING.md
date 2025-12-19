# NIST 800-53 Mapping (Lab Alignment)

This mapping shows how lab components demonstrate key NIST 800-53 control families. It is not a formal compliance assessment; it is an evidence-oriented alignment for portfolio purposes.

## Access Control (AC)
- AC-2 Account Management:
  - AD user/group lifecycle, OU structure, least privilege groups, disabled stale accounts.
- AC-3 Access Enforcement:
  - pfSense inter-VLAN firewall rules; restricted access to domain services.
- AC-6 Least Privilege:
  - Admin separation (Domain Admin vs standard users), limited lateral access between VLANs.
- AC-7 Unsuccessful Logon Attempts:
  - GPO lockout policy; SIEM alerts on bursts of failures.
- AC-17 Remote Access (lab-only):
  - VPN concepts (optional), restrict management to VLAN 99.

## Audit and Accountability (AU)
- AU-2 Event Logging:
  - Windows Security logs + Sysmon enabled; pfSense logs captured.
- AU-6 Audit Review, Analysis, and Reporting:
  - SIEM dashboards; correlation searches; daily review workflow.
- AU-12 Audit Generation:
  - Forwarding via Splunk UF / Beats; normalized ingestion pipelines.

## Configuration Management (CM)
- CM-2 Baseline Configuration:
  - Documented configs in `configs/`; standard VLAN/firewall + logging baseline.
- CM-6 Configuration Settings:
  - CIS Benchmarks applied (endpoint hardening + audit policies).
- CM-8 System Component Inventory:
  - Lab inventory documented; VM role list and network addressing.

## Incident Response (IR)
- IR-4 Incident Handling:
  - Playbooks in `attack-scenarios/RESPONSE_PLAYBOOK_TEMPLATE.md`.
- IR-5 Incident Monitoring:
  - SIEM alerts + Suricata IDS events.
- IR-6 Incident Reporting:
  - Ticket-style writeups in each scenario.
- IR-8 Incident Response Plan:
  - Defined steps: detect → triage → contain → eradicate → recover → lessons learned.

## System and Communications Protection (SC)
- SC-7 Boundary Protection:
  - pfSense as boundary device; VLAN segmentation; deny-by-default rule sets.
- SC-8 Transmission Confidentiality/Integrity (conceptual):
  - Secure network design + segmentation; optional TLS logging for web services.
- SC-24 Fail in Known State:
  - Firewall default deny; controlled allow rules.

## System and Information Integrity (SI)
- SI-3 Malicious Code Protection:
  - Detection via Suricata signatures and endpoint telemetry.
- SI-4 System Monitoring:
  - Splunk/ELK monitoring; beacon detection script; anomaly dashboards.
- SI-5 Security Alerts, Advisories, and Directives:
  - Alerting logic documented; escalation steps in playbooks.

## Risk Assessment (RA)
- RA-3 Risk Assessment:
  - Threat modeling (STRIDE/DREAD) applied to lab segments and services.
- RA-5 Vulnerability Monitoring and Scanning:
  - Nmap scanning; vuln validation; remediation notes.

## Evidence Artifacts (Suggested)
- Screenshots: VLANs, firewall rules, SIEM dashboards
- Log samples: failed logons, process creation, Suricata alerts
- Detection queries: saved searches and filters included in repo
