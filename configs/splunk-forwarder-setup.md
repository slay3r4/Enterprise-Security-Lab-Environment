# Splunk Forwarder Setup 

## On Windows Hosts
- Install Splunk Universal Forwarder
- Configure inputs for:
  - Windows Security
  - Sysmon
  - PowerShell Operational
- Forward to Splunk indexer TCP 9997

## On pfSense
- Enable remote syslog to Splunk receiver (listener)
- Capture firewall events and DHCP/DNS 
## Validate
- Confirm events are searchable
- Confirm sourcetypes are correct
