# Linux Basics Cheat Sheet 🐧💻

## Part 1: Linux Fundamentals

### What is Linux?
Linux is an open-source, Unix-like operating system kernel that forms the core of many operating systems (distributions).

### Common Linux Distributions
- **Ubuntu** - User-friendly, great for beginners
- **Debian** - Stable, foundation for many distros
- **CentOS/RHEL** - Enterprise-focused, stable
- **Fedora** - Cutting-edge features
- **Arch Linux** - DIY, highly customizable

### Linux Directory Structure
```
/           - Root directory
/bin        - Essential user binaries
/etc        - System configuration files
/home       - User home directories
/var        - Variable data (logs, etc.)
/usr        - User programs and data
/tmp        - Temporary files
/dev        - Device files
/boot       - Boot loader files
```

---

## Part 2: Basic Commands 🖥️

### File System Navigation
```bash
pwd         # Print working directory (show current location)
ls          # List files and directories
ls -l       # Detailed listing
ls -a       # Show hidden files
cd          # Change directory
cd ~        # Go to home directory
cd ..       # Go up one level
```

### File Operations
```bash
touch file.txt      # Create empty file
mkdir directory     # Create directory
mkdir -p dir1/dir2  # Create nested directories
cp file1 file2      # Copy file
cp -r dir1 dir2     # Copy directory recursively
mv file1 file2      # Move/rename file
rm file.txt         # Remove file
rm -r directory     # Remove directory recursively
rm -rf directory    # Force remove (be careful!)
```

### File Viewing & Editing
```bash
cat file.txt        # Display file content
less file.txt       # View file page by page
head file.txt       # Show first 10 lines
tail file.txt       # Show last 10 lines
tail -f file.txt    # Follow file changes (for logs)
nano file.txt       # Simple text editor
vim file.txt        # Advanced text editor
```

---

## Part 3: File Permissions & Ownership 🔐

### Understanding Permissions
```
-rwxr-xr--  1 user group 4096 Jan 01 12:00 file.txt
│ ─┬─ ─┬─ ─┬─ 
│  │   │   │
│  │   │   └─ Others: read only (r--)
│  │   └───── Group: read & execute (r-x)
│  └───────── Owner: all permissions (rwx)
└──────────── File type (- = file, d = directory)
```

### Permission Commands
```bash
chmod 755 file.txt      # Set permissions (rwxr-xr-x)
chmod u+x file.txt      # Add execute permission for owner
chmod g-w file.txt      # Remove write permission for group
chmod o=r file.txt      # Set others to read only

chown user file.txt     # Change file owner
chown user:group file.txt # Change owner and group
chgrp group file.txt    # Change file group
```

### Numeric Permission Values
```
0 = ---    4 = r--     5 = r-x     6 = rw-     7 = rwx
1 = --x
2 = -w-
3 = -wx
```

---

## Part 4: Process Management ⚙️

### Process Commands
```bash
ps               # Show current processes
ps aux           # Show all processes
top              # Interactive process viewer
htop             # Enhanced top (if installed)
kill PID         # Kill process by ID
kill -9 PID      # Force kill process
pkill process_name # Kill process by name
bg               # Send process to background
fg               # Bring process to foreground
jobs             # List background jobs
```

### System Monitoring
```bash
free -h          # Show memory usage (human readable)
df -h            # Show disk space (human readable)
du -sh directory # Show directory size
uptime           # Show system uptime and load
who              # Show logged in users
w                # Show who is logged in and what they're doing
```

---

## Part 5: Text Processing & Searching 🔍

### Searching Files
```bash
grep "pattern" file.txt      # Search for pattern in file
grep -r "pattern" directory  # Recursive search
grep -i "pattern" file.txt   # Case-insensitive search
find /path -name "*.txt"     # Find files by name
find /path -type f -name "*.log" # Find files
find /path -type d -name "dir"  # Find directories
locate file.txt              # Find file using database
```

### Text Processing
```bash
cat file.txt | grep "pattern"    # Pipe output to grep
cat file.txt | wc -l             # Count lines
cat file.txt | sort              # Sort lines
cat file.txt | uniq              # Remove duplicate lines
cat file.txt | head -n 5         # Show first 5 lines
cat file.txt | tail -n 5         # Show last 5 lines
sed 's/old/new/g' file.txt       # Replace text
awk '{print $1}' file.txt        # Print first column
```

---

## Part 6: Compression & Archives 📦

### Archive Commands
```bash
tar -cvf archive.tar files/    # Create tar archive
tar -xvf archive.tar           # Extract tar archive
tar -czvf archive.tar.gz files/ # Create compressed tar
tar -xzvf archive.tar.gz       # Extract compressed tar
tar -cjvf archive.tar.bz2 files/ # Create bzip2 compressed tar
tar -xjvf archive.tar.bz2      # Extract bzip2 compressed tar

zip archive.zip files/         # Create zip archive
unzip archive.zip              # Extract zip archive

gzip file.txt                  # Compress file (creates file.txt.gz)
gunzip file.txt.gz             # Decompress file
```

---

## Part 7: Networking 🌐

### Network Commands
```bash
ifconfig               # Network interface configuration (deprecated)
ip addr show           # Show IP addresses
ip route show          # Show routing table
ping google.com        # Test connectivity
traceroute google.com  # Trace network path
netstat -tulpn         # Show network connections
ss -tulpn              # Modern replacement for netstat
curl http://example.com # Transfer data from URL
wget http://example.com/file # Download file
ssh user@hostname      # Secure shell connection
scp file.txt user@hostname:/path # Secure copy
```

### Network Configuration Files
```bash
/etc/hosts            # Local hostname mapping
/etc/resolv.conf      # DNS configuration
/etc/network/interfaces # Network interfaces (Debian/Ubuntu)
/etc/sysconfig/network-scripts/ # Network scripts (RHEL/CentOS)
```

---

## Part 8: Package Management 📦

### Debian/Ubuntu (APT)
```bash
sudo apt update              # Update package lists
sudo apt upgrade             # Upgrade installed packages
sudo apt install package     # Install package
sudo apt remove package      # Remove package
sudo apt autoremove          # Remove unused packages
sudo apt search pattern      # Search for packages
sudo apt show package        # Show package information
sudo apt list --installed    # List installed packages
```

### RHEL/CentOS (YUM/DNF)
```bash
sudo yum update              # Update packages (older)
sudo dnf update              # Update packages (newer)
sudo yum install package     # Install package
sudo yum remove package      # Remove package
sudo yum search pattern      # Search for packages
sudo yum list installed      # List installed packages
sudo yum info package        # Show package information
```

### Arch Linux (Pacman)
```bash
sudo pacman -Syu             # Update system and packages
sudo pacman -S package       # Install package
sudo pacman -R package       # Remove package
sudo pacman -Ss pattern      # Search for packages
sudo pacman -Qs pattern      # Search installed packages
```

---

## Part 9: User Management 👥

### User Commands
```bash
whoami                  # Show current username
id                      # Show user and group IDs
sudo adduser username   # Add new user
sudo deluser username   # Delete user
sudo usermod -aG group username # Add user to group
sudo passwd username    # Change user password
sudo su - username      # Switch user
exit                    # Return to previous user
```

### Group Commands
```bash
groups                  # Show current user's groups
getent group            # List all groups
sudo groupadd groupname # Add new group
sudo groupdel groupname # Delete group
```

---

## Part 10: System Services & Daemons 🚀

### Systemd (Modern Linux)
```bash
sudo systemctl start service    # Start service
sudo systemctl stop service     # Stop service
sudo systemctl restart service  # Restart service
sudo systemctl status service   # Check service status
sudo systemctl enable service   # Enable service at boot
sudo systemctl disable service  # Disable service at boot
sudo systemctl daemon-reload    # Reload systemd configuration
journalctl -u service -f        # Follow service logs
```

### SysVinit (Older Systems)
```bash
sudo service service start      # Start service
sudo service service stop       # Stop service
sudo service service restart    # Restart service
sudo service service status     # Check service status
sudo chkconfig service on       # Enable service at boot
sudo chkconfig service off      # Disable service at boot
```

---

## Part 11: Shell Scripting Basics 📜

### Basic Script Structure
```bash
#!/bin/bash
# This is a comment
echo "Hello, World!"
```

### Variables
```bash
name="John"          # Variable assignment
echo "Hello, $name"  # Variable usage
echo "Hello, ${name}" # Alternative syntax
```

### Input/Output
```bash
read -p "Enter your name: " name  # Read input
echo "Hello, $name" > file.txt    # Output to file
echo "Appended text" >> file.txt  # Append to file
```

### Conditional Statements
```bash
if [ condition ]; then
    # commands
elif [ other_condition ]; then
    # commands
else
    # commands
fi
```

### Loops
```bash
# For loop
for i in {1..5}; do
    echo "Number: $i"
done

# While loop
count=1
while [ $count -le 5 ]; do
    echo "Count: $count"
    ((count++))
done
```

### Functions
```bash
greet() {
    echo "Hello, $1"
}
greet "Alice"  # Call function with argument
```

---

## Part 12: Useful Shortcuts & Tips 💡

### Terminal Shortcuts
```
Ctrl + C        - Interrupt/kill current process
Ctrl + D        - Exit shell (EOF)
Ctrl + Z        - Suspend current process
Ctrl + A        - Move to beginning of line
Ctrl + E        - Move to end of line
Ctrl + U        - Clear line before cursor
Ctrl + K        - Clear line after cursor
Ctrl + R        - Search command history
Tab             - Auto-complete
↑ / ↓           - Navigate command history
```

### Common Environment Variables
```bash
echo $HOME      # Home directory
echo $PATH      # Command search path
echo $USER      # Current username
echo $SHELL     # Current shell
echo $PWD       # Current working directory
```

### Configuration Files
```bash
~/.bashrc       # Bash configuration (runs for interactive shells)
~/.bash_profile # Bash profile (runs for login shells)
~/.bash_history # Command history
/etc/profile    # System-wide profile
/etc/bash.bashrc # System-wide bashrc
```

---

## Part 13: System Logs 📋

### Important Log Files
```bash
/var/log/syslog     # System logs (Debian/Ubuntu)
/var/log/messages   # System logs (RHEL/CentOS)
/var/log/auth.log   # Authentication logs
/var/log/secure     # Security logs (RHEL/CentOS)
/var/log/kern.log   # Kernel logs
/var/log/dmesg      # Kernel ring buffer
/var/log/apache2/   # Apache web server logs
/var/log/mysql/     # MySQL database logs
```

### Log Viewing Commands
```bash
sudo tail -f /var/log/syslog    # Follow system logs
sudo less /var/log/syslog       # View system logs
dmesg | less                    # View kernel messages
journalctl -f                   # Follow systemd journal
```

---

## Part 14: Security Basics 🔒

### Basic Security Commands
```bash
sudo iptables -L                # List firewall rules
sudo ufw status                 # Check Uncomplicated Firewall status
sudo chmod 600 sensitive.file   # Restrict file permissions
sudo chown root:root critical.file # Set proper ownership
sudo passwd -l username         # Lock user account
sudo passwd -u username         # Unlock user account
```

### SSH Security
```bash
# Edit /etc/ssh/sshd_config
PermitRootLogin no              # Disable root login
PasswordAuthentication no       # Disable password authentication
AllowUsers username             # Allow specific users
```

### File Integrity Checking
```bash
md5sum file.txt                 # Calculate MD5 checksum
sha256sum file.txt              # Calculate SHA256 checksum
```

---

## Part 15: Troubleshooting & Diagnostics 🐛

### Common Diagnostic Commands
```bash
dmesg                           # Kernel messages
strace command                  # Trace system calls
ltrace command                  # Trace library calls
lsof                            # List open files
tcpdump                         # Network packet analysis
vmstat 1                        # Virtual memory statistics
iostat 1                        # I/O statistics
```

### System Information
```bash
uname -a                        # Kernel version and system info
lsb_release -a                  # Distribution information
cat /etc/os-release             # OS release information
lscpu                           # CPU information
lsblk                           # Block device information
lspci                           # PCI device information
lsusb                           # USB device information
```

*Created By Shekher Saksham Shashi (AMPICS)*
