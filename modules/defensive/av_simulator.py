import hashlib

SIGNATURE_DB = {
    "e99a18c428cb38d5f260853678922e03": "WannaCry Ransomware Fragment",
    "f29a18c428cb38d5f260853678922e04": "Cobalt Strike Beacon Mock",
    "d29a18c428cb38d5f260853678922e05": "Generic Keylogger.v1"
}

def scan_string_for_malware(content):
    """
    Scans a string/binary content for malicious signatures.
    """
    file_hash = hashlib.md5(content.encode() if isinstance(content, str) else content).hexdigest()
    if file_hash in SIGNATURE_DB:
        return {"status": "INFECTED", "threat": SIGNATURE_DB[file_hash]}
    
    # Check for suspicious behaviors in strings
    suspicious = ["eval(base64_decode(", "os.system('rm -rf", ".exe --hidden"]
    for s in suspicious:
        if s in str(content):
            return {"status": "SUSPICIOUS", "threat": f"Indicator: {s}"}
            
    return {"status": "CLEAN", "threat": None}
