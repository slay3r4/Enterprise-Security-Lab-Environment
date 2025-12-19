# VLAN Design

## VLANs
- VLAN 10: Domain Services (10.10.10.0/24)
- VLAN 20: Users/Workstations (10.10.20.0/24)
- VLAN 30: Security Tooling (10.10.30.0/24)
- VLAN 99: Management (10.10.99.0/24)

## Routing
pfSense provides inter-VLAN routing and policy enforcement.

## DHCP/DNS
- pfSense DHCP per VLAN 
- DNS points to Domain Controller for domain clients
- pfSense DNS forwarder points to DC or upstream resolver for WAN traffic
