@echo off
title DiskConvert

echo.
echo ======================================
echo        Disk Converter Utility
echo ======================================
echo.

echo list disk > "%temp%\list.txt"
diskpart /s "%temp%\list.txt"
del "%temp%\list.txt"

echo.
set /p DISK=Enter disk number:

echo.
echo Select partition style
echo [1] GPT
echo [2] MBR
set /p STYLE=Choice:

if "%STYLE%"=="1" (
    set TYPE=gpt
) else if "%STYLE%"=="2" (
    set TYPE=mbr
) else (
    echo Invalid choice.
    pause
    exit /b
)

echo.
echo *************************************
echo Disk      : %DISK%
echo Partition : %TYPE%
echo *************************************
echo.
echo WARNING: ALL DATA ON THIS DISK WILL BE LOST!
set /p CONFIRM=Type YES to continue:

if /I not "%CONFIRM%"=="YES" (
    echo Cancelled.
    pause
    exit /b
)

(
echo select disk %DISK%
echo clean
echo convert %TYPE%
) > "%temp%\diskpart.txt"

diskpart /s "%temp%\diskpart.txt"

del "%temp%\diskpart.txt"

echo.
echo ======================================
echo Finished successfully.
echo ======================================
pause
