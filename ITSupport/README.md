# IT Support & Desktop Administration Cheat Sheet 💻🛠️

*Curated for freshers and entry-level IT Support Specialists / Helpdesk Engineers with technical interview questions asked as of November 2026.*

---

## Part 1: IT Support Core Fundamentals

### The ITIL Incident Management Process
1. **Identification**: Alert or user ticket logged.
2. **Logging & Categorization**: Severity (P1/Critical to P4/Low), hardware vs software vs network.
3. **Prioritization**: Impact x Urgency (SLA response time).
4. **Initial Diagnosis**: Gather symptom information, replicate issue, check recent changes.
5. **Escalation (if required)**: Tier 1 (Helpdesk) -> Tier 2 (Sysadmin / Desktop) -> Tier 3 (Network / DevOps / Engineering).
6. **Resolution & Recovery**: Verify with user that issue is solved.
7. **Incident Closure & Knowledge Base Article**: Document the fix for team reuse.

### The OSI Model (7 Layers) Troubleshooting Framework
- **Layer 7 (Application)**: HTTP, HTTPS, DNS, SMTP, SSH (Browser errors, client crashes)
- **Layer 6 (Presentation)**: SSL/TLS, Encryption, MIME
- **Layer 5 (Session)**: RPC, NetBIOS (Session management)
- **Layer 4 (Transport)**: TCP, UDP (Port communication, firewalls)
- **Layer 3 (Network)**: IP, ICMP, Routers (IP assignment, routing table, ping)
- **Layer 2 (Data Link)**: Ethernet, MAC addresses, Switches
- **Layer 1 (Physical)**: Cables, RJ45 jacks, Wi-Fi antennas, power cords

*Rule of Thumb: Always troubleshoot from bottom to top (Layer 1 to Layer 7) to avoid chasing software bugs when a cable is simply unplugged.*

---

## Part 2: Technical Interview Questions & Multiple Solutions (IT Support Freshers) 🎯

### Question 1: A user reports: "My computer says 'No Internet Access' and I can't open any websites." How do you troubleshoot and fix it?

#### Logic & Background:
Tests systematic network isolation: Is the issue local to the device, local network/DHCP, DNS, default gateway, or external ISP?

#### Troubleshooting Flow (Step-by-Step):
1. **Check Physical / Layer 1**: Is Ethernet cable firmly plugged in with green/amber link lights? Is Wi-Fi toggled on and connected to the corporate SSID?
2. **Check IP Configuration**:
   - Run `ipconfig /all` (Windows) or `ip a` (Linux).
   - If IP starts with `169.254.x.x` (APIPA - Automatic Private IP Addressing), the client failed to reach the DHCP server.
3. **Test Gateway Connectivity**:
   - `ping <default_gateway_ip>` (e.g. `ping 192.168.1.1`). If this fails, the local router/switch or VLAN is unreachable.
4. **Test Public IP Connectivity (Bypass DNS)**:
   - `ping 8.8.8.8` or `ping 1.1.1.1`.
   - If ping to 8.8.8.8 succeeds but `ping google.com` fails, the issue is **DNS resolution failure**.

#### Multiple Ways to Fix:

##### Method 1: Graphical User Interface (GUI) - Non-Technical End-User Guidance
- Turn Wi-Fi Off and On again in Windows Settings.
- Open **Settings > Network & Internet > Advanced network settings > Network reset**.
- Click **Reset now** (reinstalls network adapters and resets networking components).

##### Method 2: Windows Command Prompt (CMD)
- Run Command Prompt as Administrator:
  ```cmd
  ipconfig /release         :: Release current DHCP lease
  ipconfig /renew           :: Request new IP from DHCP server
  ipconfig /flushdns        :: Clear corrupt DNS cache
  netsh winsock reset       :: Reset Winsock catalog / TCP stack
  netsh int ip reset        :: Reinstall IPv4 stack
  ```
- Reboot the computer.

##### Method 3: PowerShell Automation (Enterprise Remote Support)
- Run via remote PowerShell (`Enter-PSSession` or Intune script):
  ```powershell
  Clear-DnsClientCache
  Restart-NetAdapter -Name "Ethernet"
  Test-NetConnection -ComputerName "google.com" -Port 443
  Resolve-DnsName -Name "companyportal.internal"
  ```

---

### Question 2: A domain user is locked out of their workstation after entering an incorrect password. How do you unlock and verify the account?

#### Logic & Background:
Active Directory account lockout policies protect against brute-force attacks after N failed attempts (typically 3 to 5).

#### Method 1: Active Directory Administrative Center / ADUC (GUI)
- **Logic**: Open **Active Directory Users and Computers (ADUC)** on domain controller / RSAT.
- **Steps**:
  1. Search for the user's username.
  2. Double-click the user and open the **Account** tab.
  3. Check the box **"Unlock account. This account is currently locked out on this Active Directory Domain Controller"**.
  4. Click **Apply** and **OK**.

#### Method 2: PowerShell ActiveDirectory Module (CLI / Automation)
- **Logic**: Use the official Microsoft Active Directory PowerShell cmdlet.
- **Commands**:
  ```powershell
  # Check if account is locked
  Get-ADUser -Identity "john.doe" -Properties LockedOut | Select-Object Name, LockedOut

  # Unlock account
  Unlock-ADAccount -Identity "john.doe"
  ```
- **Pros**: Can be scripted or run directly from helpdesk ticketing automation.

#### Method 3: Local Windows Account via Command Prompt / Net User (Workgroup / Non-domain machine)
- **Logic**: If the machine is standalone and not bound to Active Directory domain.
- **Commands**:
  ```cmd
  net user john.doe /active:yes
  net user john.doe NewPassword123!
  ```

---

### Question 3: A user's C: drive is 99% full, causing Windows crashes and sluggish performance. How do you free up disk space?

#### Logic & Background:
Full OS drives block virtual memory paging, Windows updates, and software installations.

#### Method 1: Windows GUI Tools (Storage Sense & Disk Cleanup)
- **Steps**:
  1. Press `Win + R`, type `cleanmgr /sageset:1`, select all items (Temporary files, Recycle Bin, Windows Update Cleanup), and run `cleanmgr /sagerun:1`.
  2. Enable **Settings > System > Storage > Storage Sense** for automated temp file deletion.

#### Method 2: Command Line (CMD / Batch Script)
- **Commands**:
  ```cmd
  del /q/f/s "%TEMP%\*"
  del /q/f/s "%WINDIR%\Temp\*"
  cleanmgr /verylowdisk
  Dism.exe /online /Cleanup-Image /StartComponentCleanup /ResetBase
  ```
- **Note**: `Dism.exe` removes superseded Windows update backup files, often reclaiming 5GB to 15GB.

#### Method 3: PowerShell Scripting with Analysis
- **Logic**: Find top 10 largest directories before deleting blindly:
  ```powershell
  Get-ChildItem -Path C:\ -Directory | ForEach-Object {
      [PSCustomObject]@{
          Folder = $_.FullName
          SizeGB = [math]::Round((Get-ChildItem $_.FullName -Recurse -File -ErrorAction SilentlyContinue | Measure-Object -Property Length -Sum).Sum / 1GB, 2)
      }
  } | Sort-Object SizeGB -Descending | Select-Object -First 10
  ```

---

### Question 4: How do you identify whether a computer is infected with malware or a suspicious rogue process?

#### Logic & Background:
Endpoint security is a primary responsibility for IT Support in preventing ransomware spread across internal corporate networks.

#### Method 1: Immediate Network Isolation (Containment First)
- Disconnect Ethernet cable and turn off Wi-Fi immediately to prevent lateral movement or data exfiltration.

#### Method 2: Task Manager & Resource Monitor Analysis (GUI)
- Open **Task Manager** (`Ctrl + Shift + Esc`).
- Inspect Startup apps tab, sort Processes by CPU/Memory.
- Right-click unknown high-utilization processes and choose **Open file location** and **Search online**.
- Verify digital signatures on the `.exe` file (Properties > Digital Signatures).

#### Method 3: Windows Sysinternals & Command Line (Advanced Triage)
- **Commands**:
  ```cmd
  netstat -ano | findstr ESTABLISHED   :: Check active network sockets and foreign IPs with PID
  tasklist /fi "PID eq <suspicious_pid>"
  wmic process where processid=<PID> get ExecutablePath,CommandLine
  ```
- **Tools**: Run **Autoruns** (Sysinternals) to inspect persistence mechanisms (Registry Run keys, Scheduled Tasks, Services).

---

*Created By Shekher Saksham Shashi (AMPICS)*
