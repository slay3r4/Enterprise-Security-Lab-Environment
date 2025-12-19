# pfSense Firewall Rules 

## Principles
- Default deny between VLANs
- Allow only necessary traffic to domain services
- Allow Security VLAN to receive logs from other VLANs
- Keep management restricted to VLAN 99

## Example Allow Rules
VLAN 20 (Users) → VLAN 10 (DC)
- DNS: TCP/UDP 53 to DC IP
- Kerberos: TCP/UDP 88 to DC IP
- LDAP/LDAPS: TCP 389/636 to DC IP 
- SMB: TCP 445 to DC IP 

VLAN 20 → VLAN 30 (Security)
- Splunk HEC: TCP 8088 
- Splunk UF: TCP 9997 to Splunk indexer
- Beats: TCP 5044 to Logstash
- Syslog: UDP 514 to SIEM receiver

VLAN 99 (Mgmt) → all VLANs
- RDP/WinRM/SSH only to admin hosts
- Web access to pfSense GUI

## IDS Mirror
- Mirror/inspect VLAN trunk traffic via Suricata on appropriate interface.
