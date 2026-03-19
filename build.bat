@echo off
echo [*] CYBER HUB: Building Standalone Executable...
echo [*] This process may take a few minutes (requires PyInstaller).

pip install pyinstaller

set CTK_PATH=C:\Users\marco\AppData\Roaming\Python\Python313\site-packages\customtkinter

pyinstaller --noconfirm --onefile --windowed ^
    --add-data "modules;modules" ^
    --add-data "%CTK_PATH%;customtkinter" ^
    --name "CyberHub_v3" ^
    main.py

echo [*] Build finished! Check the 'dist' folder for CyberHub_v3.exe
pause
