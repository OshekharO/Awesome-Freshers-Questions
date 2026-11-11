# IT Support & Desktop Administration Cheat Sheet 💻🛠️

*Curated for freshers and entry-level IT Support Specialists / Helpdesk Engineers with comprehensive technical interview questions asked as of November 2026.*

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
- Open **Active Directory Users and Computers (ADUC)** on domain controller / RSAT.
- Search for the user's username.
- Double-click the user and open the **Account** tab.
- Check the box **"Unlock account. This account is currently locked out on this Active Directory Domain Controller"**.
- Click **Apply** and **OK**.

#### Method 2: PowerShell ActiveDirectory Module (CLI / Automation)
- Commands:
  ```powershell
  # Check if account is locked
  Get-ADUser -Identity "john.doe" -Properties LockedOut | Select-Object Name, LockedOut

  # Unlock account
  Unlock-ADAccount -Identity "john.doe"
  ```
- Can be triggered automatically from helpdesk ticketing workflows.

#### Method 3: Local Windows Account via Command Prompt / Net User (Workgroup machine)
- Commands:
  ```cmd
  net user john.doe /active:yes
  net user john.doe NewPassword123!
  ```

---

### Question 3: A user experiences a Blue Screen of Death (BSOD) with `CRITICAL_PROCESS_DIED` or `DRIVER_IRQL_NOT_LESS_OR_EQUAL`. How do you diagnose and fix it?

#### Logic & Background:
BSOD indicates a fatal Windows kernel crash caused by corrupted system files, faulty device drivers, or defective hardware (e.g. failing RAM/SSD).

#### Method 1: System File Repair via DISM and SFC (Command Line)
- Boot into Safe Mode or Windows Recovery Environment (WinRE) Command Prompt:
  ```cmd
  # Repair Windows component store online image
  DISM /Online /Cleanup-Image /RestoreHealth

  # Scan and replace corrupted protected system files
  sfc /scannow

  # Check and repair filesystem disk errors
  chkdsk C: /f /r
  ```

#### Method 2: Windows Minidump Analysis (Root Cause Identification)
- Inspect memory dump file located at `C:\Windows\Minidump\*.dmp` using **BlueScreenView** or Microsoft **WinDbg**:
  - Run `!analyze -v` in WinDbg.
  - Inspect `MODULE_NAME` and `IMAGE_NAME` to pinpoint the exact faulty `.sys` driver (e.g. display graphics, network driver, antivirus filter driver).
  - Boot into Safe Mode and roll back or reinstall the specific driver in **Device Manager**.

#### Method 3: Hardware Diagnostics (RAM & Storage)
- **RAM Check**: Run Windows Memory Diagnostic tool (`mdsched.exe`) or MemTest86.
- **Disk Health**: Check S.M.A.R.T. status using PowerShell `Get-PhysicalDisk` or CrystalDiskInfo.

---

### Question 4: A network printer is showing "Offline" or print jobs are permanently stuck in the queue. How do you resolve it?

#### Logic & Background:
Print queue deadlocks occur when a corrupted document file locks the Windows Print Spooler service.

#### Method 1: Restart Print Spooler and Clear Queue Files (Command Prompt)
- Run as Administrator:
  ```cmd
  net stop spooler
  del /Q /F /S "%systemroot%\System32\Spool\Printers\*.*"
  net start spooler
  ```
- **Why**: Deletes stuck spool files (`.shd` and `.spl`) from disk before restarting the spooler daemon.

#### Method 2: PowerShell Service and TCP/IP Port Triage
- Commands:
  ```powershell
  Restart-Service -Name Spooler -Force
  Test-NetConnection -ComputerName "192.168.1.150" -Port 9100 # Standard RAW print port
  Get-Printer -Name "Office-Floor2" | Select-Object Name, PrinterStatus, PortName
  ```

#### Method 3: GUI Triage
- Open **Settings > Bluetooth & devices > Printers & scanners**.
- Select the printer > **Open print queue** > **Printer** menu > uncheck **"Use Printer Offline"**.
- Delete and re-add the printer via IP address rather than WSD (Web Services for Devices) which is notoriously prone to sleep/offline bugs.

---

### Question 5: A user reports that Microsoft Outlook will not open or is stuck on "Loading Profile". How do you troubleshoot?

#### Logic & Background:
Usually caused by a corrupt Outlook add-in, corrupted navigation pane cache, or bloated/corrupted local OST/PST data file.

#### Method 1: Launch in Safe Mode & Disable Add-ins
- Press `Win + R`, type `outlook.exe /safe` and press Enter.
- If Outlook opens normally in safe mode, an add-in is the culprit:
  - Go to **File > Options > Add-ins > COM Add-ins > Go**.
  - Uncheck third-party add-ins (e.g. Adobe, Zoom, Antivirus plugins) one by one to isolate the issue.

#### Method 2: Reset Navigation Pane & Data File Repair
- Clear navigation pane: `outlook.exe /resetnavpane`.
- Repair corrupted PST/OST files using the built-in Microsoft Inbox Repair Tool:
  - Run `scanpst.exe` (found in `C:\Program Files\Microsoft Office\root\Office16\scanpst.exe`).

#### Method 3: Recreate Outlook Profile / OST Data File
- Close Outlook.
- Navigate to `%localappdata%\Microsoft\Outlook` and rename the account `.ost` file to `.ost.old`.
- Open **Control Panel > Mail (Microsoft Outlook) > Show Profiles > Add**.
- Create a clean profile; Outlook will reconnect to Microsoft 365 Exchange and automatically redownload the mailbox cleanly.

---

### Question 6: A remote employee cannot connect to the corporate VPN. How do you troubleshoot?

#### Logic & Background:
Remote work relies heavily on secure VPN tunnels (Cisco AnyConnect, GlobalProtect, OpenVPN). Failures typically stem from local Wi-Fi captive portals, stale virtual network adapters, or conflicting subnets.

#### Method 1: Check Captive Portal & Internet Reachability
- Can the user open a public web browser page?
- Often, users at coffee shops or airports haven't accepted the Wi-Fi terms & conditions. Once accepted, VPN connects immediately.

#### Method 2: Reinstall / Reset Virtual TAP Adapter (Device Manager)
- In **Device Manager**, expand **Network adapters**.
- Right-click the VPN virtual adapter (e.g., Cisco AnyConnect Secure Mobility Client Virtual Miniport Adapter).
- Choose **Uninstall device**, then in VPN client select repair or reboot machine to let Windows reinstall the clean driver.

#### Method 3: Subnet Conflict & MTU Adjustment
- If the employee's home router uses the identical subnet as the corporate internal network (e.g. both use `192.168.1.0/24`), routing breaks.
- Enable **Split Tunneling** or lower MTU packet size (from 1500 to 1350) using `netsh interface ipv4 set subinterface "VPN" mtu=1350 store=persistent` to avoid packet fragmentation over home ISPs.

---

### Question 7: Remote Desktop (RDP) connection fails with "Remote Desktop can't connect to the remote computer". How do you troubleshoot?

#### Logic & Background:
Tests understanding of RDP service states, firewall port 3389 rules, and Network Level Authentication (NLA).

#### Method 1: Remote Connectivity & Port Verification (PowerShell)
- Run from helpdesk workstation:
  ```powershell
  Test-NetConnection -ComputerName "PC-ACCOUNTING-04" -Port 3389
  ```
- If `TcpTestSucceeded : False`, the host is powered off, sleeping, or port 3389 is blocked by Windows Defender Firewall.

#### Method 2: Windows Services & Firewall Check (CMD)
- Ensure the TermService service is running:
  ```cmd
  sc query TermService
  sc start TermService
  ```
- Enable RDP rule in Windows Firewall:
  ```cmd
  netsh advfirewall firewall set rule group="remote desktop" new enable=Yes
  ```

#### Method 3: Network Level Authentication (NLA) Workaround
- If user credentials fail before screen connects, NLA is rejecting the client.
- Disable NLA temporarily via registry or System Properties:
  - System Properties > Remote tab > uncheck "Allow connections only from computers running Remote Desktop with Network Level Authentication".

---

*Created By Shekher Saksham Shashi (AMPICS)*
