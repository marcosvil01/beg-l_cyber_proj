import random

def simulate_tor_connection():
    """
    Simulates the creation of a 3-hop Tor circuit.
    """
    nodes = ["1.1.1.2 (Entry)", "45.10.2.1 (Relay)", "190.44.1.9 (Exit)"]
    path = []
    
    for node in nodes:
        path.append({
            "node": node,
            "latency": random.randint(100, 300),
            "status": "Encrypted"
        })
        
    return path

def get_tor_info():
    return "The Onion Router (Tor) uses multi-layered encryption.\n" \
           "1. Entry Node: Only knows your real IP.\n" \
           "2. Middle Relay: Knows nothing but bridge IPs.\n" \
           "3. Exit Node: Decrypts the final layer (Danger: SSL is vital here)."
