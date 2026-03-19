import subprocess
import os

def run_audit():
    """
    Performs a local system security audit.
    Note: Requires administrative privileges for full accuracy.
    """
    results = []
    
    # 1. Firewall Check
    try:
        fw = subprocess.check_output("netsh advfirewall show allprofiles state", shell=True).decode()
        status = "ENABLED" if "ON" in fw.upper() else "DISABLED"
        results.append(f"[!] Firewall: {status}")
    except:
        results.append("[?] Firewall: Unknown (Permission denied)")

    # 2. Guest Account
    try:
        guest = subprocess.check_output("net user guest", shell=True, stderr=subprocess.STDOUT).decode()
        status = "ACTIVE" if "Account active               Yes" in guest else "Safe (Disabled)"
        results.append(f"[!] Guest Account: {status}")
    except:
        results.append("[!] Guest Account: Disabled (Default Safe)")

    # 3. SMBv1 Check (Legacy vulnerable protocol)
    try:
        smb = subprocess.check_output("sc query mrxsmb10", shell=True, stderr=subprocess.STDOUT).decode()
        status = "RUNNING (Vulnerable)" if "RUNNING" in smb.upper() else "Not Found (Safe)"
        results.append(f"[!] SMBv1 Status: {status}")
    except:
        results.append("[!] SMBv1 Status: Not Found / Disabled (Safe)")

    # 4. UAC Level Check
    try:
        import winreg
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System")
        uac, _ = winreg.QueryValueEx(key, "ConsentPromptBehaviorAdmin")
        status = "MAX (Always Notify)" if uac == 2 else "DEFAULT" if uac == 5 else "LOW / DISABLED"
        results.append(f"[!] UAC Security Level: {status}")
    except:
        results.append("[?] UAC Status: Access Denied")

    return results

if __name__ == "__main__":
    for item in run_audit():
        print(item)
