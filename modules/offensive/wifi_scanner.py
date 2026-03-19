import os

def get_available_networks():
    """
    Mocks or scans for Wi-Fi networks.
    """
    # Real scanning on Windows: netsh wlan show networks
    try:
        # For professional feel, we'll try to run the command
        import subprocess
        data = subprocess.check_output("netsh wlan show networks", shell=True).decode()
        return data
    except:
        return "--- MOCK SCAN RESULTS ---\n" \
               "[+] Home_WiFi - Signal: 90% - Security: WPA2-Personal\n" \
               "[+] Starbucks_Free - Signal: 40% - Security: OPEN (CAUTION)\n" \
               "[+] Office_5G - Signal: 75% - Security: WPA3-Enterprise"

def get_security_recommendation(security_type):
    if "OPEN" in security_type.upper():
        return "AVOID: Unencrypted traffic can be sniffed. Use a VPN."
    elif "WPA2" in security_type.upper():
        return "GOOD: WPA2 is standard, but ensure a strong password."
    elif "WPA3" in security_type.upper():
        return "EXCELLENT: WPA3 is the latest security standard."
    return "UNKNOWN: Verify encryption protocol."
