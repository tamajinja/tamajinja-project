#!/usr/bin/env python3
import os

def check_updates():
    print("\n🔍 Checking for available updates...")
    os.system("sudo apt update && apt list --upgradable")

def check_services():
    print("\n🔍 Checking running services...")
    os.system("systemctl list-units --type=service --state=running")

def check_ports():
    print("\n🔍 Checking open ports...")
    os.system("ss -tuln")

if __name__ == "__main__":
    print("🚀 Nancy_VPS_Engineer is running...\n")
    check_updates()
    check_services()
    check_ports()
    print("\n✅ Done.")
