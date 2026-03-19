from scapy.all import sniff, IP, TCP, UDP
import threading

def packet_callback(packet):
    """
    Called for each captured packet.
    """
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = "TCP" if TCP in packet else "UDP" if UDP in packet else "Other"
        print(f"[+] {protocol} - {ip_src} -> {ip_dst}")

def start_sniffing(interface=None, count=10, filter_type=None, callback=None):
    """
    Captures a set number of packets.
    filter_type: "tcp", "udp", "icmp", etc.
    """
    filter_str = filter_type if filter_type else ""
    print(f"[*] Sniffing on {interface if interface else 'default'} (Filter: {filter_str})...")
    
    def internal_callback(packet):
        if IP in packet:
            ip_layer = packet[IP]
            proto = "TCP" if TCP in packet else "UDP" if UDP in packet else "Other"
            mac_info = f" | MAC: {packet.src} -> {packet.dst}" if hasattr(packet, 'src') else ""
            
            info = f"[{proto}] {ip_layer.src} -> {ip_layer.dst} | TTL: {ip_layer.ttl} | SZ: {len(packet)}b{mac_info}"
            if callback:
                callback(info)
            else:
                print(f"[+] {info}")

    try:
        sniff(iface=interface, prn=internal_callback, count=count, filter=filter_str, store=0)
    except Exception as e:
        if callback:
            callback(f"ERROR: {str(e)}")
        else:
            print(f"[-] Error sniffing: {e}")

if __name__ == "__main__":
    # Example usage for standalone testing
    # Note: Requires admin/root
    # start_sniffing(count=5)
    pass
