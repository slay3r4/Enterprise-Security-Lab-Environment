# Windows Logging + Sysmon

## Enable auditing via GPO
- Logon/Logoff events
- Account logon events
- Process creation
- PowerShell logging (Module + Script Block)
- Object access (as needed)

## Sysmon 
Capture:
- Process creation
- Network connections
- Image loaded (optional)
- Registry changes (optional)

Forward logs to:
- Splunk Universal Forwarder
- or Winlogbeat to ELK
