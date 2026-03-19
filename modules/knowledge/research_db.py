def get_zeroday_history():
    return [
        {"name": "EternalBlue (CVE-2017-0144)", "impact": "Critical", "desc": "SMBv1 exploit used in WannaCry ransomware."},
        {"name": "Stuxnet (2010)", "impact": "Nation-State", "desc": "Targeted SCADA systems via multiple zero-days."},
        {"name": "Log4Shell (CVE-2021-44228)", "impact": "Critical", "desc": "Remote code execution in Log4j logging library."},
        {"name": "Heartbleed (CVE-2014-0160)", "impact": "High", "desc": "OpenSSL buffer over-read vulnerability."}
    ]

def get_research_tips():
    return [
        "Monitor CVE databases regularly (NVD, MITRE).",
        "Follow security researchers on specialized forums.",
        "Understand memory corruption fundamentals (Overflows, UAF).",
        "Practice with Capture The Flag (CTF) challenges."
    ]
