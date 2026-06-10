@echo off
title VMware Device Guard / VBS Fix
color 0A

echo ============================================
echo VMware Workstation VBS / Device Guard Fix
echo ============================================
echo.

:: Verify Administrator
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Please run this script as Administrator.
    pause
    exit /b
)

echo [1/6] Disabling Virtualization Based Security (VBS)...

reg add "HKLM\SYSTEM\CurrentControlSet\Control\DeviceGuard" ^
 /v EnableVirtualizationBasedSecurity /t REG_DWORD /d 0 /f

reg add "HKLM\SYSTEM\CurrentControlSet\Control\DeviceGuard" ^
 /v RequirePlatformSecurityFeatures /t REG_DWORD /d 0 /f

reg add "HKLM\SYSTEM\CurrentControlSet\Control\Lsa" ^
 /v LsaCfgFlags /t REG_DWORD /d 0 /f

echo.
echo [2/6] Disabling Hyper-V...

dism /online /disable-feature /featurename:Microsoft-Hyper-V-All /norestart

echo.
echo [3/6] Disabling Windows Hypervisor Platform...

dism /online /disable-feature /featurename:HypervisorPlatform /norestart

echo.
echo [4/6] Disabling Virtual Machine Platform...

dism /online /disable-feature /featurename:VirtualMachinePlatform /norestart

echo.
echo [5/6] Configuring Boot Options...

bcdedit /create {0cb3b571-2f2e-4343-a879-d86a476d7215} /d "DebugTool" /application osloader >nul 2>&1

bcdedit /set {0cb3b571-2f2e-4343-a879-d86a476d7215} path "\EFI\Microsoft\Boot\SecConfig.efi"

bcdedit /set {bootmgr} bootsequence {0cb3b571-2f2e-4343-a879-d86a476d7215}

bcdedit /set {0cb3b571-2f2e-4343-a879-d86a476d7215} loadoptions DISABLE-LSA-ISO,DISABLE-VBS

bcdedit /set hypervisorlaunchtype off

echo.
echo [6/6] Completed.
echo.
echo ============================================
echo Changes applied successfully.
echo RESTART YOUR COMPUTER NOW.
echo ============================================
echo.

pause
