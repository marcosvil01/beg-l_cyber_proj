@echo off
echo [*] CYBER HUB: Automating Environment Setup...
echo [*] Checking for Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] Error: Python not found in PATH. Please install Python 3.10+
    pause
    exit /b
)

echo [*] Installing requirements from requirements.txt...
pip install -r requirements.txt

echo [*] Setup Complete! You can now run 'python main.py' or use 'build.bat' to create an EXE.
pause
