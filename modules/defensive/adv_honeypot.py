import time
import json

def log_attack_event(event_type, source_ip, details):
    """
    Logs an attack event to a structured format.
    """
    event = {
        "timestamp": time.ctime(),
        "type": event_type,
        "source": source_ip,
        "details": details,
        "severity": "HIGH" if "exploit" in details.lower() else "LOW"
    }
    # In a real app, we'd append to a file
    return json.dumps(event, indent=2)

def get_interaction_simulation():
    return [
        {"step": 1, "action": "Port Scan Detected", "flag": "RECON"},
        {"step": 2, "action": "Brute Force Attempt on Port 22", "flag": "AUTH_FAILURE"},
        {"step": 3, "action": "Command Injection Payload Received", "flag": "EXPLOIT_ATTEMPT"},
        {"step": 4, "action": "Honeypot Decoy Successfully Engaged", "flag": "MITIGATION"}
    ]
