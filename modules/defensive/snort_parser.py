import os
import re

def parse_snort_logs(log_content):
    """
    Parses common Snort alert patterns.
    [**] [1:1000001:1] SQL Injection Attempt [**] [Priority: 1] {TCP} 192.168.1.10:80 -> 192.168.1.20:443
    """
    alerts = []
    pattern = r"\[\*\*\] \[\d+:(\d+):\d+\] (.*?) \[\*\*\] \[Priority: (\d+)\] \{(.*?)\} (\d+\.\d+\.\d+\.\d+):?(\d*) -> (\d+\.\d+\.\d+\.\d+):?(\d*)"
    
    for line in log_content.splitlines():
        match = re.search(pattern, line)
        if match:
            alerts.append({
                "SID": match.group(1),
                "MSG": match.group(2),
                "Priority": match.group(3),
                "Proto": match.group(4),
                "Src": f"{match.group(5)}:{match.group(6)}",
                "Dst": f"{match.group(7)}:{match.group(8)}"
            })
    return alerts

def get_demo_logs():
    return "[**] [1:200001:0] ET CRAWLERS Possible Scrapy User-Agent [**] [Priority: 2] {TCP} 10.0.0.5:4321 -> 180.50.2.1:80\n" \
           "[**] [1:1000001:1] SQL Injection Attempt [**] [Priority: 1] {TCP} 192.168.1.50:54321 -> 192.168.1.2:80"
