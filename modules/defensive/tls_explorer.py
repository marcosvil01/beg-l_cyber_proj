import ssl
import socket
from datetime import datetime

def get_certificate_info(hostname, port=443):
    """
    Connects to a host and retrieves the SSL certificate info.
    """
    context = ssl.create_default_context()
    try:
        with socket.create_connection((hostname, port), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                
                info = {
                    "Subject": dict(x[0] for x in cert['subject']),
                    "Issuer": dict(x[0] for x in cert['issuer']),
                    "Version": cert['version'],
                    "Expires": cert['notAfter']
                }
                return info
    except Exception as e:
        return {"error": str(e)}

def check_expiration(expiry_str):
    expiry_date = datetime.strptime(expiry_str, '%b %d %H:%M:%S %Y %Z')
    if expiry_date < datetime.now():
        return "EXPIRED ❌"
    return "Valid ✅"
