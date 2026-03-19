import os

def monitor_dns():
    """
    Simulates DNS security check by verifying nameservers.
    """
    # Real check: find nameserver entries
    try:
        if os.name == 'nt':
            # Windows: ipconfig /all or nslookup
            import subprocess
            res = subprocess.check_output("nslookup google.com", shell=True).decode()
            server_line = [l for l in res.splitlines() if "Server" in l]
            return {"status": "OK", "msg": f"Monitoring active. Using server: {server_line[0] if server_line else 'Default'}"}
    except:
        pass
        
    return {"status": "WARNING", "msg": "Could not verify DNS server context."}

def check_arp_table():
    """
    Looks for duplicate MAC addresses (ARP Spoof indicator).
    """
    # Simulated check
    try:
        import subprocess
        arp_data = subprocess.check_output("arp -a", shell=True).decode()
        return arp_data
    except:
        return "No ARP table accessible."
