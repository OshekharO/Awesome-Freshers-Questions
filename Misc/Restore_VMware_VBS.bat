@echo off
title Restore Hyper-V and VBS

bcdedit /set hypervisorlaunchtype auto

dism /online /enable-feature /featurename:Microsoft-Hyper-V-All /all /norestart
dism /online /enable-feature /featurename:HypervisorPlatform /all /norestart
dism /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

echo.
echo Hyper-V restored.
echo Restart your computer.
pause
