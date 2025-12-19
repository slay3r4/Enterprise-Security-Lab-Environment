<# Collects failed logons (Event ID 4625) from local Windows Security log.
Usage:
  powershell -ExecutionPolicy Bypass -File .\windows_failed_logons.ps1 -Hours 24
#>

param(
  [int]$Hours = 24
)

$start = (Get-Date).AddHours(-$Hours)

Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4625; StartTime=$start} |
  Select-Object TimeCreated,
                @{n="TargetUser";e={$_.Properties[5].Value}},
                @{n="Workstation";e={$_.Properties[13].Value}},
                @{n="SourceIP";e={$_.Properties[19].Value}},
                @{n="FailureReason";e={$_.Properties[8].Value}} |
  Sort-Object TimeCreated -Descending
