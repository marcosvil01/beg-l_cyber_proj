import customtkinter as ctk
from PIL import Image
import os
import threading
import time

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
            {"id": 2, "name": "Password Cracker", "category": "Offensive", "desc": "Pro dictionary & brute-force cracker."},
            {"id": 3, "name": "Network Sniffer", "category": "Offensive", "desc": "Detailed packet header analyzer."},
            {"id": 4, "name": "Basic Keylogger", "category": "Offensive", "desc": "Keystroke logger for demo."},
            {"id": 5, "name": "Forensic Tool", "category": "Forensics", "desc": "Deep EXIF & file extractor."},
            {"id": 6, "name": "Cyber Lab Setup", "category": "Knowledge", "desc": "Self-learning lab guide."},
            {"id": 7, "name": "File Encryption", "category": "Defensive", "desc": "AES-256 secure locker."},
            {"id": 8, "name": "Phishing Simulator", "category": "Offensive", "desc": "Email awareness tool."},
            {"id": 9, "name": "Wi-Fi Security", "category": "Forensics", "desc": "Live signal & security scanner."},
            {"id": 10, "name": "Network Scanner", "category": "Offensive", "desc": "Nmap-style port scanner."},
            {"id": 11, "name": "Firewall Rule Manager", "category": "Defensive", "desc": "Win Firewall automation."},
            {"id": 12, "name": "2FA Hub", "category": "Defensive", "desc": "Encrypted TOTP vault."},
            {"id": 13, "name": "Secure Web App", "category": "Knowledge", "desc": "Vulnerable vs Secure demo."},
            {"id": 14, "name": "Snort IDS Logs", "category": "Defensive", "desc": "IDS log file parser."},
            {"id": 15, "name": "Vuln Finder", "category": "Forensics", "desc": "Audit Windows misconfigurations."},
            {"id": 16, "name": "DNS Spoof Monitor", "category": "Defensive", "desc": "ARP/DNS poisoning alert."},
            {"id": 17, "name": "Antivirus Sim", "category": "Defensive", "desc": "Signature-based scanner."},
            {"id": 18, "name": "Activity Monitor", "category": "Forensics", "desc": "Live CPU/RAM visualizations."},
            {"id": 19, "name": "Malware Analyzer", "category": "Forensics", "desc": "Deep static PE dissection."},
            {"id": 20, "name": "TLS/SSL Explorer", "category": "Defensive", "desc": "Certificate validator."},
            {"id": 21, "name": "Zero-Day Research", "category": "Knowledge", "desc": "Exploit history database."},
            {"id": 22, "name": "Tor Proxy Hub", "category": "Knowledge", "desc": "Tor connection manager."},
            {"id": 23, "name": "Advanced Honeypot", "category": "Defensive", "desc": "High-interaction shell sim."},
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
        self.geometry("600x550")
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Header
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

        self.setup_module_ui()
        
        self.lift()
        self.attributes("-topmost", True)
        self.after(500, lambda: self.attributes("-topmost", False))

    def setup_module_ui(self):
        pid = self.project["id"]
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
            15: self.ui_vulnerability_scanner,
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
        if pid in dispatch: dispatch[pid]()

    # --- UIs ---

    def ui_honeypot(self):
        from modules.defensive.honeypot import start_honeypot
        ctk.CTkLabel(self.content_frame, text="Listening Ports (22, 80, 443):").pack(pady=10)
        pe = ctk.CTkEntry(self.content_frame, width=200); pe.insert(0, "22, 80, 2222"); pe.pack(pady=5)
        def run():
            ports = [int(p.strip()) for p in pe.get().split(",")]
            threading.Thread(target=start_honeypot, args=(ports,), daemon=True).start()
            self.parent.log(f"Honeypot active on {ports}")
        ctk.CTkButton(self.content_frame, text="Start Trap", command=run).pack(pady=10)

    def ui_password_cracker(self):
        from modules.offensive.password_cracker import crack_password, brute_force
        tab = ctk.CTkTabview(self.content_frame, height=380); tab.pack(fill="both", expand=True)
        t_dict = tab.add("Dictionary"); t_brute = tab.add("Brute-Force")
        
        # Dict
        ctk.CTkLabel(t_dict, text="Target MD5/SHA256:").pack(pady=5)
        h_ent = ctk.CTkEntry(t_dict, width=350); h_ent.pack(pady=5)
        type_m = ctk.CTkOptionMenu(t_dict, values=["md5", "sha256"]); type_m.pack(pady=5)
        def run_d():
            res = crack_password(h_ent.get(), type_m.get(), "modules/offensive/passwords.txt")
            self.parent.log(res)
        ctk.CTkButton(t_dict, text="Attack", command=run_d).pack(pady=10)

        # Brute Force PRO
        ctk.CTkLabel(t_brute, text="Target Hash:").pack(pady=5)
        b_ent = ctk.CTkEntry(t_brute, width=350); b_ent.pack(pady=5)
        self.char_vars = {"lower": ctk.BooleanVar(value=True), "upper": ctk.BooleanVar(value=False), "digits": ctk.BooleanVar(value=True), "special": ctk.BooleanVar(value=False)}
        f = ctk.CTkFrame(t_brute, fg_color="transparent"); f.pack(pady=5)
        for k, v in self.char_vars.items(): ctk.CTkCheckBox(f, text=k, variable=v, width=70).pack(side="left")
        p = ctk.CTkProgressBar(t_brute, width=350); p.set(0); p.pack(pady=10)
        def run_b():
            sets = [k for k, v in self.char_vars.items() if v.get()]
            def task():
                res = brute_force(b_ent.get(), "sha256", 4, sets, lambda v: p.set(v))
                self.parent.log(res)
            threading.Thread(target=task, daemon=True).start()
        ctk.CTkButton(t_brute, text="Start Pro Attack", command=run_b).pack(pady=10)

    def ui_sniffer(self):
        from modules.offensive.sniffer import start_sniffing
        ctk.CTkLabel(self.content_frame, text="Protocol (tcp/udp):").pack(pady=5)
        pm = ctk.CTkOptionMenu(self.content_frame, values=["", "tcp", "udp", "icmp"]); pm.pack(pady=5)
        rb = ctk.CTkTextbox(self.content_frame, height=250, font=("Consolas", 10)); rb.pack(pady=10, fill="both", expand=True)
        def run():
            rb.delete("0.0", "end")
            threading.Thread(target=start_sniffing, args=(None, 15, pm.get(), lambda i: rb.insert("end", f"{i}\n")), daemon=True).start()
        f = ctk.CTkFrame(self.content_frame, fg_color="transparent"); f.pack(pady=5)
        ctk.CTkButton(f, text="Start", command=run).pack(side="left", padx=5)
        ctk.CTkButton(f, text="💾 Save", fg_color="green", command=lambda: open("sniff.txt","w").write(rb.get("0.0","end"))).pack(side="left", padx=5)

    def ui_vulnerability_scanner(self):
        from modules.forensics.vuln_scanner import run_audit
        rb = ctk.CTkTextbox(self.content_frame, height=300, font=("Consolas", 11)); rb.pack(pady=10, fill="both", expand=True)
        def run():
            rb.delete("0.0", "end")
            for line in run_audit(): rb.insert("end", f"{line}\n")
        ctk.CTkButton(self.content_frame, text="Run Security Audit", command=run).pack(pady=10)

    def ui_malware_analyzer(self):
        from modules.forensics.malware_analyzer import analyze_file
        rb = ctk.CTkTextbox(self.content_frame, height=300, font=("Consolas", 10)); rb.pack(pady=10, fill="both", expand=True)
        def run():
            from tkinter import filedialog
            f = filedialog.askopenfilename()
            if not f: return
            res = analyze_file(f)
            rb.delete("0.0", "end")
            rb.insert("end", f"FILE: {res['Analysis']['File']}\nMD5:  {res['Analysis']['MD5']}\nENTR: {res['Analysis']['Entropy']}\n\n")
            rb.insert("end", "[!] SUSPICIOUS APIs:\n" + "\n".join([f" - {a}" for a in res['Indicators']['Suspicious_APIs']]))
        ctk.CTkButton(self.content_frame, text="Select Binary", command=run).pack(pady=10)

    def ui_wifi_scanner(self):
        from modules.offensive.wifi_scanner import get_available_networks, get_security_recommendation, brute_force_wifi
        tab = ctk.CTkTabview(self.content_frame, height=400); tab.pack(fill="both", expand=True)
        t_scan = tab.add("Network Scan"); t_brute = tab.add("Brute-Force")
        
        # Scan Tab
        sc = ctk.CTkScrollableFrame(t_scan, height=300); sc.pack(fill="both", expand=True, padx=10, pady=5)
        def scan():
            for w in sc.winfo_children(): w.destroy()
            for n in get_available_networks():
                f = ctk.CTkFrame(sc, fg_color="#333", corner_radius=10); f.pack(fill="x", pady=2, padx=5)
                ctk.CTkLabel(f, text=f"📶 {n['ssid']}", font=ctk.CTkFont(weight="bold")).pack(side="left", padx=10)
                b = ctk.CTkProgressBar(f, width=80); b.pack(side="right", padx=10); b.set(n['signal']/100)
                ctk.CTkLabel(f, text=f"{n['security']}", font=ctk.CTkFont(size=9), text_color="gray").pack(side="left")
        ctk.CTkButton(t_scan, text="Refresh Scan", command=scan).pack(pady=5); scan()

        # Brute-Force Tab
        ctk.CTkLabel(t_brute, text="Target SSID:").pack(pady=5)
        s_ent = ctk.CTkEntry(t_brute, width=250); s_ent.pack(pady=5)
        ctk.CTkLabel(t_brute, text="Common Passwords (comma separated):").pack(pady=5)
        p_ent = ctk.CTkEntry(t_brute, width=250); p_ent.insert(0, "12345678, password, admin123, qwertyuiop"); p_ent.pack(pady=5)
        
        pb = ctk.CTkProgressBar(t_brute, width=300); pb.set(0); pb.pack(pady=10)
        curr_p = ctk.CTkLabel(t_brute, text="Status: Ready", text_color="gray")
        curr_p.pack()

        def run_bf():
            target = s_ent.get()
            plist = [p.strip() for p in p_ent.get().split(",")]
            def task():
                res = brute_force_wifi(target, plist, lambda v, pwd: [self.after(0, lambda: [pb.set(v), curr_p.configure(text=f"Testing: {pwd}")])])
                if res["success"]:
                    self.parent.log(f"SUCCESS! Found password for {target}: {res['password']}")
                    curr_p.configure(text=f"FOUND: {res['password']}", text_color="green")
                else:
                    self.parent.log(f"Brute-force failed for {target}.")
                    curr_p.configure(text="Finished: No password found", text_color="red")
            threading.Thread(target=task, daemon=True).start()
        
        ctk.CTkButton(t_brute, text="Launch Audit", command=run_bf).pack(pady=10)

    def ui_2fa(self):
        from modules.defensive.two_factor import load_secrets, save_secret, generate_totp_secret, get_current_code
        lf = ctk.CTkScrollableFrame(self.content_frame, height=250); lf.pack(fill="both", expand=True, padx=10, pady=5)
        def refresh():
            for w in lf.winfo_children(): w.destroy()
            for l, s in load_secrets().items():
                r = ctk.CTkFrame(lf); r.pack(fill="x", pady=2)
                ctk.CTkLabel(r, text=l).pack(side="left", padx=10)
                ctk.CTkLabel(r, text=get_current_code(s), font=ctk.CTkFont(size=18, weight="bold"), text_color="cyan").pack(side="right", padx=10)
        refresh()
        ctk.CTkButton(self.content_frame, text="Add Account (Auto-Gen)", command=lambda: [save_secret("New", generate_totp_secret()), refresh()]).pack(pady=10)

    def ui_activity_monitor(self):
        from modules.forensics.activity_monitor import get_system_stats
        cb = ctk.CTkProgressBar(self.content_frame); cb.pack(pady=10, padx=20, fill="x")
        mb = ctk.CTkProgressBar(self.content_frame); mb.pack(pady=10, padx=20, fill="x")
        rb = ctk.CTkTextbox(self.content_frame, height=150); rb.pack(pady=10, fill="both", expand=True)
        def refresh():
            s = get_system_stats()
            cb.set(s['cpu_percent']/100); mb.set(s['memory_percent']/100)
            rb.delete("0.0", "end")
            for p in s['processes']: rb.insert("end", f"{p['name']}: {p['cpu']}%\n")
            self.after(2000, refresh)
        refresh()

    def ui_adv_honeypot(self):
        from modules.defensive.adv_honeypot import simulate_interaction
        rb = ctk.CTkTextbox(self.content_frame, height=350, font=("Consolas", 11)); rb.pack(pady=10, fill="both", expand=True)
        def run():
            rb.delete("0.0", "end")
            for entry in simulate_interaction(22):
                rb.insert("end", f"{entry}\n"); self.update(); time.sleep(0.3)
        ctk.CTkButton(self.content_frame, text="Run Session Sim", command=lambda: threading.Thread(target=run, daemon=True).start()).pack(pady=10)

    def ui_metadata_extractor(self):
        from modules.forensics.metadata_extractor import extract_metadata
        rb = ctk.CTkTextbox(self.content_frame, height=300, font=("Consolas", 10)); rb.pack(pady=10, fill="both", expand=True)
        def run():
            from tkinter import filedialog
            f = filedialog.askopenfilename()
            if not f: return
            res = extract_metadata(f)
            rb.delete("0.0", "end")
            for k, v in res.get("Forensic Meta", {}).items(): rb.insert("end", f"{k}: {v}\n")
        ctk.CTkButton(self.content_frame, text="Analyze Image", command=run).pack(pady=10)

    def ui_keylogger(self):
        from modules.offensive.keylogger import start_keylogger
        ctk.CTkButton(self.content_frame, text="Start Logger", command=lambda: [threading.Thread(target=start_keylogger, args=("keylog.txt",), daemon=True).start(), self.parent.log("Keylogger Active")]).pack(pady=50)

    def ui_encryption(self):
        from modules.defensive.encryption import generate_key, encrypt_file, decrypt_file
        ctk.CTkButton(self.content_frame, text="Encrypt", command=lambda: [encrypt_file(ctk.filedialog.askopenfilename(), generate_key())]).pack(pady=10)
        ctk.CTkButton(self.content_frame, text="Decrypt", command=lambda: [decrypt_file(ctk.filedialog.askopenfilename(), open("key.key","rb").read())]).pack(pady=10)

    def ui_firewall_manager(self):
        from modules.defensive.firewall_manager import add_block_rule, list_firewall_rules
        lbl = ctk.CTkLabel(self.content_frame, text="Firewall Port Blocker", font=ctk.CTkFont(weight="bold"))
        lbl.pack(pady=10)
        p_ent = ctk.CTkEntry(self.content_frame, placeholder_text="Enter Port to Block (e.g. 445)")
        p_ent.pack(pady=5)
        def run():
            cmd = add_block_rule("CyberHub-Block", p_ent.get())
            self.parent.log(f"Generated: {cmd}")
        ctk.CTkButton(self.content_frame, text="Generate Block Rule", command=run).pack(pady=10)

    def ui_lab_setup(self): self.show_text_file("modules/knowledge/lab_guide.md")
    def ui_phishing(self):
        from modules.offensive.phishing_simulator import launch_phishing_template
        ctk.CTkLabel(self.content_frame, text="Phishing Awareness Simulator", font=ctk.CTkFont(weight="bold")).pack(pady=10)
        ctk.CTkLabel(self.content_frame, text="Launches a local template to train users on identifying\nsuspicious login pages.", wraplength=400).pack(pady=10)
        def run():
            if launch_phishing_template(): self.parent.log("Safe Phishing Template Launched.")
            else: self.parent.log("Error: Template not found.")
        ctk.CTkButton(self.content_frame, text="Launch Template", command=run).pack(pady=20)

    def ui_network_scanner(self): 
        from modules.offensive.network_scanner import run_scanner
        ctk.CTkLabel(self.content_frame, text="Nmap-style Port Scanner", font=ctk.CTkFont(weight="bold")).pack(pady=10)
        ent = ctk.CTkEntry(self.content_frame, width=200); ent.insert(0, "127.0.0.1"); ent.pack(pady=10)
        rb = ctk.CTkTextbox(self.content_frame, height=200); rb.pack(pady=10, fill="both", expand=True)
        def run():
            rb.delete("0.0", "end")
            rb.insert("end", f"[*] Scanning {ent.get()} (Ports 1-1024)...\n")
            def task():
                ports = run_scanner(ent.get(), 1, 1024)
                rb.insert("end", f"[+] Open ports: {ports}\n")
            threading.Thread(target=task, daemon=True).start()
        ctk.CTkButton(self.content_frame, text="Start Scan", command=run).pack(pady=10)

    def ui_web_app(self): 
        ctk.CTkLabel(self.content_frame, text="Secure Web Application Demo", font=ctk.CTkFont(weight="bold")).pack(pady=10)
        ctk.CTkLabel(self.content_frame, text="This tool tests local web safety. Ensure the Flask server\nis running in the background.", wraplength=400).pack(pady=10)
        def run_web():
            import webbrowser
            webbrowser.open("http://127.0.0.1:5000")
        ctk.CTkButton(self.content_frame, text="Open Browser Demo", command=run_web).pack(pady=50)

    def ui_snort_parser(self):
        from modules.defensive.snort_parser import parse_snort_logs, get_demo_logs
        rb = ctk.CTkTextbox(self.content_frame, height=300, font=("Consolas", 10))
        rb.pack(pady=10, fill="both", expand=True)
        def run():
            rb.delete("0.0", "end")
            alerts = parse_snort_logs(get_demo_logs())
            for a in alerts:
                rb.insert("end", f"[!] {a['MSG']} (PRIO: {a['Priority']})\n    SRC: {a['Src']} -> DST: {a['Dst']}\n\n")
        ctk.CTkButton(self.content_frame, text="Analyze Demo Logs", command=run).pack(pady=10)

    def ui_dns_spoof_monitor(self):
        from modules.defensive.dns_monitor import monitor_dns, check_arp_table
        rb = ctk.CTkTextbox(self.content_frame, height=300, font=("Consolas", 10))
        rb.pack(pady=10, fill="both", expand=True)
        def run():
            rb.delete("0.0", "end")
            dns = monitor_dns()
            rb.insert("end", f"[*] DNS STATUS: {dns['status']}\n{dns['msg']}\n\n[*] ARP SCAN:\n{check_arp_table()}")
        ctk.CTkButton(self.content_frame, text="Perform Security Check", command=run).pack(pady=10)

    def ui_av_simulator(self):
        from modules.defensive.av_simulator import scan_string_for_malware
        ctk.CTkLabel(self.content_frame, text="Signature Scanner", font=ctk.CTkFont(weight="bold")).pack(pady=10)
        ent = ctk.CTkEntry(self.content_frame, width=400, placeholder_text="Enter string or file path to scan")
        ent.pack(pady=10)
        def run():
            res = scan_string_for_malware(ent.get())
            self.parent.log(f"AV Result: {res['status']} | Threat: {res['threat']}")
        ctk.CTkButton(self.content_frame, text="Run Scan", command=run).pack(pady=10)

    def ui_tls_explorer(self):
        from modules.defensive.tls_explorer import get_certificate_info
        ctk.CTkLabel(self.content_frame, text="TLS/SSL Explorer", font=ctk.CTkFont(weight="bold")).pack(pady=10)
        ent = ctk.CTkEntry(self.content_frame, width=300); ent.insert(0, "google.com"); ent.pack(pady=10)
        rb = ctk.CTkTextbox(self.content_frame, height=200); rb.pack(pady=10, fill="both", expand=True)
        def run():
            rb.delete("0.0", "end")
            info = get_certificate_info(ent.get())
            rb.insert("end", f"Certificate for {ent.get()}:\n{info}")
        ctk.CTkButton(self.content_frame, text="Probe Domain", command=run).pack(pady=10)

    def ui_research_db(self): self.show_text_file("modules/knowledge/research_db.py")
    
    def ui_tor_hub(self):
        from modules.knowledge.tor_hub import simulate_tor_connection
        ctk.CTkLabel(self.content_frame, text="Tor Circuit Simulator Management", font=ctk.CTkFont(weight="bold")).pack(pady=10)
        rb = ctk.CTkTextbox(self.content_frame, height=200); rb.pack(pady=10, fill="both", expand=True)
        def run():
            path = simulate_tor_connection()
            rb.insert("end", f"New Circuit: {' -> '.join([n['node'] for n in path])}\n")
        ctk.CTkButton(self.content_frame, text="Establish New Circuit", command=run).pack(pady=10)

    def ui_gpu_crack_theory(self): self.show_text_file("modules/offensive/gpu_crack_theory.py")
    def ui_browser_ext_info(self): self.parent.log("Extension folder: modules/web/ext/")

    def show_text_file(self, path):
        txt = ctk.CTkTextbox(self.content_frame, height=350)
        txt.pack(fill="both", expand=True, padx=10, pady=10)
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                txt.insert("0.0", f.read())
        txt.configure(state="disabled")

if __name__ == "__main__":
    app = CyberHubApp()
    app.mainloop()
