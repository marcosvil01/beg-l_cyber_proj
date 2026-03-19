# 🔐 CyberHub: Ultimate Master Suite (v3.0 - Deep Refinement)

CyberHub is a professional-grade, modular cybersecurity education and testing platform. It integrates **25 specialized tools** into a unified, glassmorphic dashboard built with Python and CustomTkinter. Version 3.0 introduces utility-grade logic, real-time visualizations, and hardened security.

> [!WARNING]
> **LEGAL DISCLAIMER**: Use this tool ONLY for educational purposes and testing on networks/systems you own. Unauthorized use is illegal.

---

## 🚀 25 Professional Modules

CyberHub is organized into four distinct security phases, now enhanced with "x100" logic depth:

### ⚔️ Offensive (Red Team)
1. **Multi-Port Honeypot**: Decoy service with high-interaction shell simulation.
2. **Password Cracker PRO**: Support for custom character sets and real-time brute-force tracking.
3. **Network Sniffer**: Detailed dissection (MAC, TTL, SZ) with save-to-log capability.
4. **Keylogger**: Stealthy keystroke monitoring for training.
5. **Wi-Fi Scanner**: Live discovery with visual signal strength bars and security audits.
6. **Network Port Scanner**: High-speed discovery of open services.
7. **Phishing Simulator**: Security awareness training with HTML templates.
8. **GPU Crack Theory**: Performance benchmarking and parallel hashing overview.

### 🛡️ Defensive (Blue Team)
9. **AES-256 Encryption**: Secure file locker with automated key management.
10. **2FA Hub (Encrypted)**: TOTP vault hardened with **AES-256 local storage encryption**.
11. **Firewall Manager**: Rule generation for Windows advanced firewall automation.
12. **Snort Log Parser**: Deep formatting of IDS/IPS alerts for forensic review.
13. **DNS & ARP Monitor**: Real-time detection of spoofing and network anomalies.
14. **Antivirus Sim**: Signature-based scanning against a specialized threat database.
15. **TLS/SSL Explorer**: Real-time probe and validation of domain certificates.

### 🔍 Forensics & Analysis
16. **Malware Analyzer**: Static PE dissection (suspicious APIs, Anti-VM/Debug strings).
17. **Vuln Audit**: Windows security configuration scanner (SMBv1, UAC, Guest checks).
18. **Metadata Extractor**: High-value forensic recovery (Camera, GPS, Stats) from images.
19. **Activity Monitor**: Visual CPU and RAM usage trackers with process monitoring.
20. **Zero-Day Research DB**: Historical repository of famous exploits and research notes.

### 🌐 Web & Lab
21. **Secure Web App**: Flask demo showcasing SQLi and XSS prevention.
22. **Tor Proxy Hub**: Simulated circuit routing and darknet architecture guide.
23. **Safety Browser Extension**: Security-focused manifest V3 template for Chrome.
24. **Cyber Lab Setup Guide**: Master guide for VirtualBox, Kali, and lab hardening.
25. **Decoy Assets**: Advanced situational awareness and honeypot interaction logs.

---

## 🛠️ Installation & Setup (One-Click)

1.  **Automated Setup**: Run `setup.bat` to install all dependencies automatically.
2.  **Manual Setup**:
   ```bash
   pip install -r requirements.txt
   ```
3.  **Launch Dashboard**: Run `CyberHub_Launcher.bat` or `python main.py`.

## 📦 Creating an Executable (.exe)
To generate a standalone version of CyberHub for Windows:
1. Run `build.bat`.
2. Find your executable in the newly created `dist/` folder.

## ✨ Features
- **Utility-Grade Logic**: No more simple placeholders; tools perform real system audits and packet dissection.
- **Glassmorphic UI**: Sleek, modern dark mode with micro-animations and focus-locked project windows.
- **Real-Time Visualization**: Progress bars for crackers and signal bars for scanners.
- **Encrypted Storage**: 2FA secrets are encrypted locally using the `cryptography` library.
- **Background Threading**: Heavy tasks run asynchronously to keep the UI smooth and responsive.

Developed with 100x effort by **Antigravity** for **Marco**.
