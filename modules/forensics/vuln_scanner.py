import subprocess
import os

def check_firewall():
    try:
        output = subprocess.check_output("netsh advfirewall show allprofiles state", shell=True).decode()
        return "ON" if "ON" in output.upper() else "OFF"
    except:
        return "Unknown"

def check_guest_account():
    try:
        output = subprocess.check_output("net user guest", shell=True).decode()
        return "Active" if "Yes" in output else "Disabled"
    except:
        return "Disabled / Not found"

def check_open_shares():
    try:
        output = subprocess.check_output("net share", shell=True).decode()
        return [line.split()[0] for line in output.split("\n")[4:] if line.strip()]
    except:
        return []

def run_audit():
    results = []
    results.append(f"[?] Firewall State: {check_firewall()}")
    results.append(f"[?] Guest Account: {check_guest_account()}")
    shares = check_open_shares()
    results.append(f"[?] Open Shares: {', '.join(shares) if shares else 'None'}")
    return results

if __name__ == "__main__":
    for item in run_audit():
        print(item)
