import socket
import threading
import datetime

def start_honeypot(ports=[22, 23, 80, 443], log_file="honeypot_log.txt"):
    """
    Starts multiple socket listeners to simulate various services and log connection attempts.
    """
    def handle_client(client_sock, addr, port):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_msg = f"[{timestamp}] ALERT: Connection on port {port} from {addr[0]}:{addr[1]}\n"
        print(log_msg.strip())
        
        with open(log_file, "a") as f:
            f.write(log_msg)
        
        try:
            # Send a generic banner or interactive prompt based on port
            if port == 22:
                client_sock.send(b"SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0.1\n")
            elif port == 80:
                client_sock.send(b"HTTP/1.1 200 OK\nServer: Apache/2.4.41 (Ubuntu)\n\n<html><body><h1>It Works!</h1></body></html>")
            else:
                client_sock.send(b"Access Denied\n")
        except:
            pass
        finally:
            client_sock.close()

    def listen_on_port(port):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            server.bind(("0.0.0.0", port))
            server.listen(5)
            while True:
                client, addr = server.accept()
                threading.Thread(target=handle_client, args=(client, addr, port), daemon=True).start()
        except Exception as e:
            print(f"[-] Error on port {port}: {e}")
        finally:
            server.close()

    threads = []
    for p in ports:
        t = threading.Thread(target=listen_on_port, args=(p,), daemon=True)
        t.start()
        threads.append(t)
    
    return f"Honeypot active on ports: {ports}"

if __name__ == "__main__":
    # start_honeypot()
    pass
