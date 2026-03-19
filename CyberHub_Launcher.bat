@echo off
echo [*] Starting CyberHub Dashboard...
python main.py
if %errorlevel% neq 0 (
    echo [!] App crashed or Python not installed. Try running setup.bat first.
    pause
)
