import customtkinter as ctk
from PIL import Image
import os

# --- Configuration ---
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class CyberHubApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("CyberHub - Beginner Cybersecurity Projects Suite")
        self.geometry("1100x700")

        # Set grid layout 1x2 (Sidebar and Main content)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # --- Sidebar ---
        self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(6, weight=1)

        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="CYBER HUB", font=ctk.CTkFont(size=20, weight="bold", family="Orbitron"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # --- SEARCH BAR ---
        self.search_entry = ctk.CTkEntry(self.sidebar_frame, placeholder_text="🔍 Search Projects...")
        self.search_entry.grid(row=1, column=0, padx=20, pady=10)
        self.search_entry.bind("<KeyRelease>", lambda e: self.filter_projects())

        self.sidebar_button_all = ctk.CTkButton(self.sidebar_frame, text="All Projects", command=lambda: self.select_category("All"))
        self.sidebar_button_all.grid(row=2, column=0, padx=20, pady=10)

        self.sidebar_button_off = ctk.CTkButton(self.sidebar_frame, text="Offensive", command=lambda: self.select_category("Offensive"))
        self.sidebar_button_off.grid(row=3, column=0, padx=20, pady=10)

        self.sidebar_button_def = ctk.CTkButton(self.sidebar_frame, text="Defensive", command=lambda: self.select_category("Defensive"))
        self.sidebar_button_def.grid(row=4, column=0, padx=20, pady=10)

        self.sidebar_button_for = ctk.CTkButton(self.sidebar_frame, text="Forensics", command=lambda: self.select_category("Forensics"))
        self.sidebar_button_for.grid(row=5, column=0, padx=20, pady=10)

        self.sidebar_button_edu = ctk.CTkButton(self.sidebar_frame, text="Knowledge", command=lambda: self.select_category("Knowledge"))
        self.sidebar_button_edu.grid(row=6, column=0, padx=20, pady=10)

        self.appearance_mode_label = ctk.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["Dark", "Light", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # --- Main Content ---
        self.main_content = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.main_content.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        self.main_content.grid_columnconfigure(0, weight=1)
        self.main_content.grid_rowconfigure(1, weight=1)

        self.header_label = ctk.CTkLabel(self.main_content, text="Dashboard - All Projects", font=ctk.CTkFont(size=24, weight="bold"))
        self.header_label.grid(row=0, column=0, sticky="w", pady=(0, 20))

        # Scrollable Grid for Project Cards
        self.scrollable_frame = ctk.CTkScrollableFrame(self.main_content, label_text="Project Catalog")
        self.scrollable_frame.grid(row=1, column=0, sticky="nsew")
        self.scrollable_frame.grid_columnconfigure((0, 1, 2), weight=1)

        # Projects Data
        self.projects = [
            {"id": 1, "name": "Basic Honeypot", "category": "Defensive", "desc": "Simple trap to catch attackers."},
            {"id": 2, "name": "Password Cracker", "category": "Offensive", "desc": "Dictionary-based cracker."},
            {"id": 3, "name": "Network Sniffer", "category": "Offensive", "desc": "Packet header analyzer."},
            {"id": 4, "name": "Basic Keylogger", "category": "Offensive", "desc": "Keystroke logger for demo."},
            {"id": 5, "name": "Forensic Tool", "category": "Forensics", "desc": "EXIF metadata extractor."},
            {"id": 6, "name": "Cyber Lab Setup", "category": "Knowledge", "desc": "Self-learning lab guide."},
            {"id": 7, "name": "File Encryption", "category": "Defensive", "desc": "AES-256 secure locker."},
            {"id": 8, "name": "Phishing Simulator", "category": "Offensive", "desc": "Email awareness tool."},
            {"id": 9, "name": "Wi-Fi Security", "category": "Forensics", "desc": "Local WLAN scanner."},
            {"id": 10, "name": "Network Scanner", "category": "Offensive", "desc": "Nmap-style port scanner."},
            {"id": 11, "name": "Firewall Rule Manager", "category": "Defensive", "desc": "Win Firewall automation."},
            {"id": 12, "name": "2FA Hub", "category": "Defensive", "desc": "TOTP token generator."},
            {"id": 13, "name": "Secure Web App", "category": "Knowledge", "desc": "Vulnerable vs Secure demo."},
            {"id": 14, "name": "Snort IDS Logs", "category": "Defensive", "desc": "IDS log file parser."},
            {"id": 15, "name": "Vuln Finder", "category": "Forensics", "desc": "OS misconfiguration checker."},
            {"id": 16, "name": "DNS Spoof Monitor", "category": "Defensive", "desc": "ARP/DNS poisoning alert."},
            {"id": 17, "name": "Antivirus Sim", "category": "Defensive", "desc": "Signature-based scanner."},
            {"id": 18, "name": "Activity Monitor", "category": "Forensics", "desc": "Live system monitoring."},
            {"id": 19, "name": "Malware Analyzer", "category": "Forensics", "desc": "PE header static analysis."},
            {"id": 20, "name": "TLS/SSL Explorer", "category": "Defensive", "desc": "Certificate validator."},
            {"id": 21, "name": "Zero-Day Research", "category": "Knowledge", "desc": "Exploit history database."},
            {"id": 22, "name": "Tor Proxy Hub", "category": "Knowledge", "desc": "Tor connection manager."},
            {"id": 23, "name": "Advanced Honeypot", "category": "Defensive", "desc": "High-interaction logging."},
            {"id": 24, "name": "GPU Crack Theory", "category": "Offensive", "desc": "Performance benchmarking."},
            {"id": 25, "name": "Safety Browser Ext", "category": "Knowledge", "desc": "Chrome security extension."},
        ]

        self.render_project_cards("All")

        # --- Console Output ---
        self.console_frame = ctk.CTkFrame(self.main_content, height=150)
        self.console_frame.grid(row=2, column=0, sticky="ew", pady=(20, 0))
        self.console_frame.grid_columnconfigure(0, weight=1)
        
        self.console_label = ctk.CTkLabel(self.console_frame, text="Terminal Output", font=ctk.CTkFont(size=12, weight="bold"))
        self.console_label.pack(anchor="w", padx=10, pady=2)
        
        self.console_text = ctk.CTkTextbox(self.console_frame, height=120, fg_color="black", text_color="green")
        self.console_text.pack(fill="both", expand=True, padx=5, pady=5)
        self.console_text.insert("0.0", "Welcome to CyberHub. Ready to analyze...\n")
        self.console_text.configure(state="disabled")

    def render_project_cards(self, category):
        # Clear existing cards
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        filtered_projects = [p for p in self.projects if p["category"] == category or category == "All"]
        
        row, col = 0, 0
        for project in filtered_projects:
            self.create_card(project, row, col)
            col += 1
            if col > 2:
                col = 0
                row += 1

    def create_card(self, project, row, col):
        card = ctk.CTkFrame(self.scrollable_frame, width=250, height=180, corner_radius=15, border_width=1, border_color="#333")
        card.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
        card.grid_propagate(False)

        title = ctk.CTkLabel(card, text=project["name"], font=ctk.CTkFont(size=16, weight="bold"), wraplength=200)
        title.pack(pady=(15, 5), padx=10)

        cat_label = ctk.CTkLabel(card, text=project["category"], font=ctk.CTkFont(size=10), text_color="cyan")
        cat_label.pack()

        desc = ctk.CTkLabel(card, text=project["desc"], font=ctk.CTkFont(size=11), wraplength=220, text_color="gray")
        desc.pack(pady=10, padx=10)

        btn = ctk.CTkButton(card, text="Launch", height=30, width=100, command=lambda p=project: self.launch_project(p))
        btn.pack(side="bottom", pady=15)

    def select_category(self, category):
        self.header_label.configure(text=f"Dashboard - {category} Projects")
        self.filter_projects(category)

    def filter_projects(self, category=None):
        if category is None:
            # Get current category from header label text
            header_text = self.header_label.cget("text")
            category = header_text.split(" - ")[1].split(" ")[0]
            
        query = self.search_entry.get().lower()
        filtered = [
            p for p in self.projects 
            if (category == "All" or p["category"] == category)
            and (query in p["name"].lower() or query in p["desc"].lower())
        ]
        
        # Clear existing cards
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
            
        row, col = 0, 0
        for project in filtered:
            self.create_card(project, row, col)
            col += 1
            if col > 2:
                col = 0
                row += 1

    def launch_project(self, project):
        self.log(f"Launching {project['name']}...")
        
        # Create a new window for the project
        window = ProjectWindow(self, project)
        window.lift()
        window.attributes('-topmost', True)
        window.focus_force()
        # window.attributes('-topmost', False) # Optional: release after focus
        window.focus()

    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)

    def log(self, message):
        from datetime import datetime
        now = datetime.now().strftime("%H:%M:%S")
        if hasattr(self, "console_text") and self.console_text:
            self.console_text.configure(state="normal")
            self.console_text.insert("end", f"[{now}] {message}\n")
            self.console_text.see("end")
            self.console_text.configure(state="disabled")
        else:
            print(f"[{now}] {message}")

class ProjectWindow(ctk.CTkToplevel):
    def __init__(self, parent, project):
        super().__init__(parent)
        self.parent = parent
        self.project = project
        self.title(f"CyberHub - {project['name']}")
        self.geometry("600x500")
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Header with Category Icon
        cat_icons = {"Offensive": "⚔️", "Defensive": "🛡️", "Forensics": "🔍", "Knowledge": "🌐", "Web": "🔗"}
        icon = cat_icons.get(project["category"], "⚙️")
        
        self.header_frame = ctk.CTkFrame(self, height=60, fg_color="transparent")
        self.header_frame.grid(row=0, column=0, sticky="ew", padx=20, pady=(20, 10))
        
        self.header = ctk.CTkLabel(self.header_frame, text=f"{icon} {project['name']}", font=ctk.CTkFont(size=24, weight="bold"))
        self.header.pack(side="left")
        
        self.cat_tag = ctk.CTkLabel(self.header_frame, text=project["category"].upper(), font=ctk.CTkFont(size=10, weight="bold"), 
                                    fg_color="#1f538d", corner_radius=10, width=80)
        self.cat_tag.pack(side="right", padx=10)

        # Content Area
        self.content_frame = ctk.CTkFrame(self, corner_radius=15)
        self.content_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=10)
        self.content_frame.grid_columnconfigure(0, weight=1)

        # Load specific UI based on project
        self.setup_module_ui()
        
        # Ensure window is visible and on top
        self.lift()
        self.attributes("-topmost", True)
        self.after(500, lambda: self.attributes("-topmost", False)) # Stay on top initially but allow moving

    def setup_module_ui(self):
        pid = self.project["id"]
        
        # Mapping dispatch to dedicated UI methods
        dispatch = {
            1: self.ui_honeypot,
            2: self.ui_password_cracker,
            3: self.ui_sniffer,
            4: self.ui_keylogger,
            5: self.ui_metadata_extractor,
            6: self.ui_lab_setup,
            7: self.ui_encryption,
            8: self.ui_phishing,
            9: self.ui_wifi_scanner,
            10: self.ui_network_scanner,
            11: self.ui_firewall_manager,
            12: self.ui_2fa,
            13: self.ui_web_app,
            14: self.ui_snort_parser,
            15: self.ui_vuln_scanner,
            16: self.ui_dns_spoof_monitor,
            17: self.ui_av_simulator,
            18: self.ui_activity_monitor,
            19: self.ui_malware_analyzer,
            20: self.ui_tls_explorer,
            21: self.ui_research_db,
            22: self.ui_tor_hub,
            23: self.ui_adv_honeypot,
            24: self.ui_gpu_crack_theory,
            25: self.ui_browser_ext_info
        }
        
        if pid in dispatch:
            dispatch[pid]()
        else:
            lbl = ctk.CTkLabel(self.content_frame, text="Project implementation in progress...", font=ctk.CTkFont(slant="italic"))
            lbl.pack(pady=50)
            lbl.pack(pady=50)

    # --- Module Specific UIs ---
    
    def ui_honeypot(self):
        from modules.defensive.honeypot import start_honeypot
        import threading
        
        ctk.CTkLabel(self.content_frame, text="Ports to Listen (comma separated):").pack(pady=(10, 0))
        port_entry = ctk.CTkEntry(self.content_frame, width=200)
        port_entry.insert(0, "22, 80, 443, 2222")
        port_entry.pack(pady=5)
        
        status_label = ctk.CTkLabel(self.content_frame, text="Status: Stopped", text_color="red")
        status_label.pack(pady=10)
        
        def run_hp():
            try:
                ports = [int(p.strip()) for p in port_entry.get().split(",")]
                status_label.configure(text=f"Status: Running on {ports}", text_color="green")
                threading.Thread(target=start_honeypot, args=(ports,), daemon=True).start()
                self.log(f"Honeypot started on {ports}")
            except Exception as e:
                self.log(f"Error starting honeypot: {e}")

        ctk.CTkButton(self.content_frame, text="Start Multi-Port Honeypot", command=run_hp).pack(pady=10)

    def ui_password_cracker(self):
        from modules.offensive.password_cracker import crack_password, brute_force
        
        tabview = ctk.CTkTabview(self.content_frame, height=350)
        tabview.pack(fill="both", expand=True)
        tab_dict = tabview.add("Dictionary")
        tab_brute = tabview.add("Brute Force")

        # --- Dictionary Tab ---
        ctk.CTkLabel(tab_dict, text="Target Hash:").pack(pady=5)
        hash_entry = ctk.CTkEntry(tab_dict, width=400)
        hash_entry.pack(pady=5)
        hash_type_dict = ctk.CTkOptionMenu(tab_dict, values=["md5", "sha256"])
        hash_type_dict.pack(pady=5)

        progress_bar = ctk.CTkProgressBar(tab_dict, width=400)
        progress_bar.set(0)
        progress_bar.pack(pady=10)

        res_label = ctk.CTkLabel(tab_dict, text="", text_color="yellow")
        res_label.pack()

        def update_progress(val):
            progress_bar.set(val)

        def run_crack():
            res_label.configure(text="Cracking...")
            import threading
            def task():
                res = crack_password(hash_entry.get(), hash_type_dict.get(), "modules/offensive/passwords.txt", update_progress)
                res_label.configure(text=res)
            threading.Thread(target=task).start()

        ctk.CTkButton(tab_dict, text="Run Dictionary Attack", command=run_crack).pack(pady=10)

        # --- Brute Force Tab ---
        ctk.CTkLabel(tab_brute, text="Target Hash:").pack(pady=5)
        b_hash_entry = ctk.CTkEntry(tab_brute, width=400)
        b_hash_entry.pack(pady=5)
        hash_type_brute = ctk.CTkOptionMenu(tab_brute, values=["md5", "sha256"])
        hash_type_brute.pack(pady=5)
        b_progress = ctk.CTkProgressBar(tab_brute, width=400)
        b_progress.set(0)
        b_progress.pack(pady=10)
        b_res = ctk.CTkLabel(tab_brute, text="", text_color="yellow")
        b_res.pack()

        def run_brute():
            b_res.configure(text="Brute-forcing...")
            import threading
            def task():
                res = brute_force(b_hash_entry.get(), hash_type_brute.get(), 4, lambda v: b_progress.set(v))
                b_res.configure(text=res)
            threading.Thread(target=task).start()

        ctk.CTkButton(tab_brute, text="Run Brute Force (Max 4 chars)", command=run_brute).pack(pady=10)

    def ui_sniffer(self):
        from modules.offensive.sniffer import start_sniffing
        import threading
        from scapy.all import IP, TCP, UDP
        
        ctk.CTkLabel(self.content_frame, text="Filter Protocol:").pack(pady=(10, 0))
        protocol_var = ctk.CTkOptionMenu(self.content_frame, values=["", "tcp", "udp", "icmp"])
        protocol_var.pack(pady=5)

        ctk.CTkLabel(self.content_frame, text="Captures (Count):").pack(pady=(5, 0))
        count_entry = ctk.CTkEntry(self.content_frame, width=100)
        count_entry.insert(0, "10")
        count_entry.pack(pady=5)
        
        res_box = ctk.CTkTextbox(self.content_frame, height=200)
        res_box.pack(pady=10, fill="both", expand=True)

        def run_sniff():
            count = int(count_entry.get())
            proto = protocol_var.get()
            res_box.insert("end", f"Starting capture of {count} packets (Filter: {proto})...\n")
            
            def cb(pkt):
                if IP in pkt:
                    p = "TCP" if TCP in pkt else "UDP" if UDP in pkt else "IP"
                    res_box.insert("end", f"[{p}] {pkt[IP].src} -> {pkt[IP].dst}\n")
                    res_box.see("end")

            threading.Thread(target=start_sniffing, args=(None, count, proto, cb), daemon=True).start()

        ctk.CTkButton(self.content_frame, text="Start Filtered Sniffer", command=run_sniff).pack(pady=10)

    def ui_forensic_tool(self):
        # Inline implementation for metadata
        from PIL import Image
        from PIL.ExifTags import TAGS
        
        def select_file():
            from tkinter import filedialog
            file_path = filedialog.askopenfilename()
            if not file_path: return
            
            try:
                img = Image.open(file_path)
                exif = img._getexif()
                res_box.delete("0.0", "end")
                if exif:
                    for tag, value in exif.items():
                        tag_name = TAGS.get(tag, tag)
                        res_box.insert("end", f"{tag_name}: {value}\n")
                else:
                    res_box.insert("end", "No EXIF metadata found.")
            except Exception as e:
                res_box.insert("end", f"Error: {e}")

        ctk.CTkButton(self.content_frame, text="Select Image to Analyze", command=select_file).pack(pady=20)
        res_box = ctk.CTkTextbox(self.content_frame, height=200)
        res_box.pack(pady=10, fill="both", expand=True)

    def ui_encryption(self):
        from modules.defensive.encryption import generate_key, encrypt_file, decrypt_file
        
        def do_encrypt():
            from tkinter import filedialog
            f = filedialog.askopenfilename()
            if not f: return
            key = generate_key()
            encrypt_file(f, key)
            self.log(f"Encrypted {f}. Key saved to key.key")

        def do_decrypt():
            from tkinter import filedialog
            f = filedialog.askopenfilename()
            if not f: return
            # Assumes key.key exists
            try:
                key = open("key.key", "rb").read()
                decrypt_file(f, key)
                self.log(f"Decrypted {f}")
            except:
                self.log("Error: key.key not found or invalid.")

        ctk.CTkButton(self.content_frame, text="Encrypt File (Auto Key)", command=do_encrypt).pack(pady=10)
        ctk.CTkButton(self.content_frame, text="Decrypt File (Load key.key)", command=do_decrypt).pack(pady=10)

    def ui_2fa(self):
        from modules.defensive.two_factor import load_secrets, save_secret, generate_totp_secret, get_current_code
        
        ctk.CTkLabel(self.content_frame, text="Managed 2FA Accounts", font=ctk.CTkFont(size=14, weight="bold")).pack(pady=10)
        
        list_frame = ctk.CTkScrollableFrame(self.content_frame, height=200)
        list_frame.pack(fill="both", expand=True, padx=10, pady=5)

        def refresh_list():
            for widget in list_frame.winfo_children():
                widget.destroy()
            secrets = load_secrets()
            for label, secret in secrets.items():
                row = ctk.CTkFrame(list_frame)
                row.pack(fill="x", pady=2)
                ctk.CTkLabel(row, text=f"{label}:").pack(side="left", padx=10)
                code_lbl = ctk.CTkLabel(row, text=get_current_code(secret), font=ctk.CTkFont(size=16, weight="bold"), text_color="cyan")
                code_lbl.pack(side="right", padx=10)

        refresh_list()

        # Add New Account
        add_frame = ctk.CTkFrame(self.content_frame)
        add_frame.pack(fill="x", padx=10, pady=10)
        name_entry = ctk.CTkEntry(add_frame, placeholder_text="Account Name", width=150)
        name_entry.pack(side="left", padx=5)
        
        def add_acc():
            name = name_entry.get()
            if not name: return
            new_secret = generate_totp_secret()
            save_secret(name, new_secret)
            self.log(f"Added 2FA account: {name}")
            refresh_list()

        ctk.CTkButton(add_frame, text="Add Account", command=add_acc, width=100).pack(side="right", padx=5)
        ctk.CTkButton(self.content_frame, text="Refresh Codes", command=refresh_list).pack(pady=5)

    def ui_keylogger(self):
        from modules.offensive.keylogger import start_keylogger
        import threading
        
        status_label = ctk.CTkLabel(self.content_frame, text="Status: Stopped", text_color="red")
        status_label.pack(pady=10)
        
        def run_kl():
            status_label.configure(text="Status: Active (Logging to keylog.txt)", text_color="green")
            threading.Thread(target=start_keylogger, args=("keylog.txt",), daemon=True).start()

        ctk.CTkButton(self.content_frame, text="Start Keylogger", command=run_kl).pack(pady=10)

    def ui_vuln_scanner(self):
        from modules.forensics.vuln_scanner import run_audit
        
        res_box = ctk.CTkTextbox(self.content_frame, height=200)
        res_box.pack(pady=10, fill="both", expand=True)
        
        def run():
            res_box.delete("0.0", "end")
            res_box.insert("end", "[*] Running System Audit...\n")
            for line in run_audit():
                res_box.insert("end", f"{line}\n")

        ctk.CTkButton(self.content_frame, text="Run Audit", command=run).pack(pady=10)

    def ui_malware_analyzer(self):
        from modules.forensics.malware_analyzer import analyze_file
        
        def select_file():
            from tkinter import filedialog
            f = filedialog.askopenfilename()
            if not f: return
            
            res_box.delete("0.0", "end")
            res_box.insert("end", f"[*] Analyzing {f}...\n")
            
            try:
                results = analyze_file(f)
                res_box.insert("end", f"[+] Size: {results['size']} bytes\n")
                res_box.insert("end", f"[+] MD5: {results['md5']}\n")
                res_box.insert("end", f"[+] Entropy: {results['entropy']:.2f}\n")
                res_box.insert("end", f"[+] Strings Count: {results['strings_count']}\n")
                
                if results['suspicious_strings']:
                    res_box.insert("end", "\n[!] Potential Indicators:\n")
                    for s in results['suspicious_strings']:
                        res_box.insert("end", f"  - {s}\n")
                else:
                    res_box.insert("end", "\n[+] No obvious suspicious strings found.\n")
            except Exception as e:
                res_box.insert("end", f"[-] Error: {e}\n")

        ctk.CTkButton(self.content_frame, text="Analyze Binary (Deep Static)", command=select_file).pack(pady=20)
        res_box = ctk.CTkTextbox(self.content_frame, height=250)
        res_box.pack(pady=10, fill="both", expand=True)

    def ui_web_app(self):
        ctk.CTkLabel(self.content_frame, text="Secure Web App Demo (Flask)", font=ctk.CTkFont(size=14, weight="bold")).pack(pady=10)
        ctk.CTkLabel(self.content_frame, text="This demo launches a local server showing\nhow to prevent SQL Injection and XSS.", wraplength=400).pack(pady=5)
        
        def launch():
            import webbrowser
            # We would start the flask app here
            self.log("Starting local Flask server on port 5000...")
            webbrowser.open("http://127.0.0.1:5000")

        ctk.CTkButton(self.content_frame, text="Launch Demo", command=launch).pack(pady=20)

    def ui_network_scanner(self):
        from modules.offensive.network_scanner import run_scanner
        
        ctk.CTkLabel(self.content_frame, text="Target IP:").pack(pady=(10, 0))
        ip_entry = ctk.CTkEntry(self.content_frame, width=200)
        ip_entry.insert(0, "127.0.0.1")
        ip_entry.pack(pady=5)
        
        res_box = ctk.CTkTextbox(self.content_frame, height=200)
        
        def run_scan():
            target = ip_entry.get()
            res_box.pack(pady=10, fill="both", expand=True)
            res_box.insert("end", f"Scanning {target}...\n")
            
            # Run in thread to avoid freezing UI
            def task():
                ports = run_scanner(target, 1, 1024)
                res_box.insert("end", f"Open ports: {ports}\n")
            
            import threading
            threading.Thread(target=task).start()

        ctk.CTkButton(self.content_frame, text="Scan Ports", command=run_scan).pack(pady=10)

    def ui_metadata_extractor(self):
        from modules.forensics.metadata_extractor import extract_metadata
        def select_file():
            from tkinter import filedialog
            f = filedialog.askopenfilename()
            if not f: return
            data = extract_metadata(f)
            res_box.delete("0.0", "end")
            for k, v in data.items():
                if k == "EXIF":
                    res_box.insert("end", "[EXIF DATA]\n")
                    for tk, tv in v.items():
                        res_box.insert("end", f"  {tk}: {tv}\n")
                else:
                    res_box.insert("end", f"{k}: {v}\n")
        ctk.CTkButton(self.content_frame, text="Select Image to Analyze", command=select_file).pack(pady=20)
        res_box = ctk.CTkTextbox(self.content_frame, height=250)
        res_box.pack(pady=10, fill="both", expand=True)

    def ui_lab_setup(self):
        ctx_file = "modules/knowledge/lab_guide.md"
        content = open(ctx_file, "r", encoding="utf-8").read() if os.path.exists(ctx_file) else "Guide not found."
        txt = ctk.CTkTextbox(self.content_frame, height=350)
        txt.pack(fill="both", expand=True, padx=10, pady=10)
        txt.insert("0.0", content)
        txt.configure(state="disabled")

    def ui_phishing(self):
        from modules.offensive.phishing_simulator import launch_phishing_template, get_awareness_tips
        ctk.CTkLabel(self.content_frame, text="Awareness Tips", font=ctk.CTkFont(weight="bold")).pack(pady=5)
        tips = "\n".join([f"- {t}" for t in get_awareness_tips()])
        ctk.CTkLabel(self.content_frame, text=tips, wraplength=500, justify="left").pack(pady=10)
        
        def run():
            if launch_phishing_template():
                self.log("Launched phishing awareness page.")
            else:
                self.log("Error: Phishing template file missing.")
        ctk.CTkButton(self.content_frame, text="Launch Phishing Simulation", command=run).pack(pady=20)

    def ui_wifi_scanner(self):
        from modules.offensive.wifi_scanner import get_available_networks
        res_box = ctk.CTkTextbox(self.content_frame, height=300)
        res_box.pack(pady=10, fill="both", expand=True)
        def scan():
            res_box.delete("0.0", "end")
            res_box.insert("end", "[*] Scanning...\n")
            res_box.insert("end", get_available_networks())
        ctk.CTkButton(self.content_frame, text="Perform WLAN Scan", command=scan).pack(pady=10)

    def ui_firewall_manager(self):
        from modules.defensive.firewall_manager import add_block_rule, list_firewall_rules
        ctk.CTkLabel(self.content_frame, text="Target Port:").pack(pady=5)
        p_entry = ctk.CTkEntry(self.content_frame)
        p_entry.pack(pady=5)
        def do_block():
            cmd = add_block_rule("CyberHub-Block", p_entry.get())
            self.log(f"Generated Command: {cmd}")
            self.log("Note: Actual execution requires Administrative terminal.")
        ctk.CTkButton(self.content_frame, text="Generate Block Command", command=do_block).pack(pady=10)

    def ui_snort_parser(self):
        from modules.defensive.snort_parser import parse_snort_logs, get_demo_logs
        res_box = ctk.CTkTextbox(self.content_frame, height=250)
        res_box.pack(pady=10, fill="both", expand=True)
        def run():
            logs = get_demo_logs()
            alerts = parse_snort_logs(logs)
            res_box.delete("0.0", "end")
            for a in alerts:
                res_box.insert("end", f"[!] {a['MSG']} (P{a['Priority']})\n    From {a['Src']} to {a['Dst']}\n\n")
        ctk.CTkButton(self.content_frame, text="Parse Demo Alert Logs", command=run).pack(pady=10)

    def ui_dns_spoof_monitor(self):
        from modules.defensive.dns_monitor import monitor_dns, check_arp_table
        res_box = ctk.CTkTextbox(self.content_frame, height=300)
        res_box.pack(pady=10, fill="both", expand=True)
        def run():
            dns = monitor_dns()
            arp = check_arp_table()
            res_box.insert("end", f"== DNS STATUS: {dns['status']} ==\n{dns['msg']}\n\n")
            res_box.insert("end", f"== ARP TABLE ==\n{arp}\n")
        ctk.CTkButton(self.content_frame, text="Run Security Check", command=run).pack(pady=10)

    def ui_av_simulator(self):
        from modules.defensive.av_simulator import scan_string_for_malware
        ctk.CTkLabel(self.content_frame, text="Scan Input Data / File Path:").pack(pady=5)
        s_entry = ctk.CTkEntry(self.content_frame, width=400)
        s_entry.pack(pady=5)
        def run():
            res = scan_string_for_malware(s_entry.get())
            self.log(f"Result: {res['status']} - {res['threat'] if res['threat'] else 'No threats'}")
        ctk.CTkButton(self.content_frame, text="Run Signature Scan", command=run).pack(pady=10)

    def ui_activity_monitor(self):
        from modules.forensics.activity_monitor import get_system_stats
        
        ctk.CTkLabel(self.content_frame, text="CPU Usage:").pack(pady=(10, 0))
        cpu_bar = ctk.CTkProgressBar(self.content_frame)
        cpu_bar.pack(pady=5, padx=20, fill="x")
        
        ctk.CTkLabel(self.content_frame, text="Memory Usage:").pack(pady=(10, 0))
        mem_bar = ctk.CTkProgressBar(self.content_frame)
        mem_bar.pack(pady=5, padx=20, fill="x")
        
        res_box = ctk.CTkTextbox(self.content_frame, height=200)
        res_box.pack(pady=20, fill="both", expand=True)
        
        def refresh():
            stats = get_system_stats()
            cpu_val = stats['cpu_percent'] / 100
            mem_val = stats['memory_percent'] / 100
            cpu_bar.set(cpu_val)
            mem_bar.set(mem_val)
            
            res_box.delete("0.0", "end")
            res_box.insert("end", f"CPU: {stats['cpu_percent']}%\n")
            res_box.insert("end", f"RAM: {stats['memory_percent']}%\n\nTop Processes:\n")
            for p in stats['processes']:
                res_box.insert("end", f"- {p['name']}: {p['cpu']}%\n")
                
        ctk.CTkButton(self.content_frame, text="Refresh Metrics", command=refresh).pack(pady=10)
        refresh()

    def ui_tls_explorer(self):
        from modules.defensive.tls_explorer import get_certificate_info, check_expiration
        ctk.CTkLabel(self.content_frame, text="Domain (e.g. google.com):").pack(pady=5)
        d_entry = ctk.CTkEntry(self.content_frame)
        d_entry.insert(0, "google.com")
        d_entry.pack(pady=5)
        def run():
            info = get_certificate_info(d_entry.get())
            self.log(f"Certificate Info for {d_entry.get()}: {info}")
        ctk.CTkButton(self.content_frame, text="Analyze SSL", command=run).pack(pady=10)

    def ui_research_db(self):
        from modules.knowledge.research_db import get_zeroday_history
        hist = get_zeroday_history()
        res_box = ctk.CTkTextbox(self.content_frame, height=350)
        res_box.pack(pady=10, fill="both", expand=True)
        for zd in hist:
            res_box.insert("end", f"NAME: {zd['name']}\nDESC: {zd['desc']}\nIMPACT: {zd['impact']}\n\n")

    def ui_tor_hub(self):
        from modules.knowledge.tor_hub import simulate_tor_connection, get_tor_info
        ctk.CTkLabel(self.content_frame, text=get_tor_info(), wraplength=450).pack(pady=10)
        def run():
            path = simulate_tor_connection()
            self.log(f"Tor Circuit: {' -> '.join([n['node'] for n in path])}")
        ctk.CTkButton(self.content_frame, text="Simulate Circuit", command=run).pack(pady=10)

    def ui_adv_honeypot(self):
        from modules.defensive.adv_honeypot import get_interaction_simulation
        import threading
        res_box = ctk.CTkTextbox(self.content_frame, height=300)
        res_box.pack(pady=10, fill="both", expand=True)
        def run():
            steps = get_interaction_simulation()
            for s in steps:
                res_box.insert("end", f"[*] {s['action']} (Flag: {s['flag']})\n")
                self.update_idletasks()
                import time
                time.sleep(0.5)
        ctk.CTkButton(self.content_frame, text="Run High-Interaction Sim", command=lambda: threading.Thread(target=run, daemon=True).start()).pack(pady=10)

    def ui_gpu_crack_theory(self):
        from modules.offensive.gpu_crack_theory import get_gpu_vs_cpu_stats, get_theory_overview
        ctk.CTkLabel(self.content_frame, text=get_theory_overview(), wraplength=500).pack(pady=10)
        stats = get_gpu_vs_cpu_stats()
        for k, v in stats.items():
            ctk.CTkLabel(self.content_frame, text=f"{k}: {v}", text_color="cyan").pack()

    def ui_browser_ext_info(self):
        ctk.CTkLabel(self.content_frame, text="Safety Browser Extension Template", font=ctk.CTkFont(weight="bold")).pack(pady=10)
        ctk.CTkLabel(self.content_frame, text="Files located at: modules/web/ext/\n\nTo install:\n1. Open chrome://extensions\n2. Enable 'Developer Mode'\n3. Load unpacked -> Select the modules/web/ext folder.", wraplength=450).pack(pady=10)
        ctk.CTkButton(self.content_frame, text="Open Extension Folder", command=lambda: os.startfile(os.path.abspath("modules/web/ext/"))).pack(pady=20)

    def log(self, message):
        self.parent.log(message)

if __name__ == "__main__":
    app = CyberHubApp()
    app.mainloop()
