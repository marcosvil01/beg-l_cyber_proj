import subprocess
import os

def list_firewall_rules():
    """
    Simulates or lists Windows Firewall rules using netsh.
    """
    try:
        # This requires admin for real output, returning mock if fails
        result = subprocess.check_output("netsh advfirewall firewall show rule name=all", shell=True)
        return result.decode()
    except:
        return "Admin privileges required to list rules or not on Windows."

def add_block_rule(name, port, protocol="TCP"):
    """
    Adds a block rule to Windows Firewall.
    WARNING: Requires administrative privileges.
    """
    command = f"netsh advfirewall firewall add rule name=\"{name}\" dir=in action=block protocol={protocol} localport={port}"
    return command # Return command for UI to show what WOULD happen if admin

def get_block_status(port):
    """
    Check if a port is commonly blocked.
    """
    common_blocked = ["445", "139", "137"]
    return str(port) in common_blocked
