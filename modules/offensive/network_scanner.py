import socket
import threading
from concurrent.futures import ThreadPoolExecutor

def scan_port(ip, port, open_ports):
    """
    Attempts to connect to a port to see if it's open.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            if s.connect_ex((ip, port)) == 0:
                open_ports.append(port)
    except:
        pass

def run_scanner(target_ip, start_port=1, end_port=1024, max_threads=100):
    """
    Runs a multi-threaded port scan on the target IP.
    """
    open_ports = []
    
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        for port in range(start_port, end_port + 1):
            executor.submit(scan_port, target_ip, port, open_ports)
            
    open_ports.sort()
    return open_ports

if __name__ == "__main__":
    # Example usage
    target = "127.0.0.1"
    print(f"Scanning {target} for open ports (1-1024)...")
    results = run_scanner(target)
    print(f"Open ports: {results}")
