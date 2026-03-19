# Beginner Cyber Lab Setup Guide

Building your own lab is the first step to becoming a security professional.

## 1. Hypervisor Selection
- **VirtualBox (Free)**: Recommended for beginners.
- **VMware Workstation Player**: Good alternative.

## 2. Operating Systems
- **Kali Linux**: The pentester's Swiss Army Knife. [Download](https://www.kali.org/get-kali/)
- **Metasploitable 2**: An intentionally vulnerable Linux VM for practice.
- **Windows 10/11**: For testing offensive tools in a real-world environment.

## 3. Network Configuration
- **NAT Network**: Allows VMs to talk to each other and the internet.
- **Host-Only Adapter**: Safer for high-risk exploits (no internet access).

## 4. First Steps
1. Update Kali: `sudo apt update && sudo apt upgrade -y`
2. Scan your lab network: `nmap -sn 10.0.2.0/24`
3. Practice basic SSH and Telnet connections.

> [!WARNING]
> Never run offensive tools against networks or devices you do not own.
