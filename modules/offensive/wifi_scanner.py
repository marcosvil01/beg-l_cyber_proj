import subprocess
import re

def get_available_networks():
    """
    Scans for Wi-Fi networks and returns structured data.
    """
    networks = []
    try:
        data = subprocess.check_output("netsh wlan show networks mode=bssid", shell=True).decode('utf-8', errors='ignore')
        
        # Simple regex parsing for SSID and Signal
        ssids = re.findall(r"SSID \d+ : (.+)", data)
        signals = re.findall(r"Signal\s+: (\d+)%", data)
        auths = re.findall(r"Autenticaci.+n\s+: (.+)", data) # Handles Spanish OS
        
        for i in range(min(len(ssids), len(signals))):
            networks.append({
                "ssid": ssids[i].strip(),
                "signal": int(signals[i]),
                "security": auths[i].strip() if i < len(auths) else "Unknown"
            })
            
    except Exception as e:
        # Fallback if command fails
        networks = [
            {"ssid": "Home_WiFi (Mock)", "signal": 90, "security": "WPA2-Personal"},
            {"ssid": "Guest_Net (Mock)", "signal": 45, "security": "Open"},
            {"ssid": "Starbucks (Mock)", "signal": 30, "security": "Open"}
        ]
        
    return networks

def get_security_recommendation(security_type):
    st = security_type.upper()
    if "OPEN" in st or "ABIERTO" in st:
        return "CRITICAL: No encryption. Avoid for sensitive tasks."
    elif "WPA2" in st:
        return "SAFE: Standard WPA2 protection."
    elif "WPA3" in st:
        return "EXCELLENT: Modern WPA3 protocol."
    return "CAUTION: Uncommon protocol. Check manually."
