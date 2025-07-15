#!/usr/bin/env python3
import os

ROOT_DIR = os.path.expanduser("~/tamajinja-project")

def check_structure(directory):
    print("🔍 Checking directory structure consistency...")
    expected_dirs = [
        "nancy/github",
        "nancy/vps",
        "nancy/architecture",
        "nancy/meta"
    ]
    for d in expected_dirs:
        path = os.path.join(ROOT_DIR, d)
        if not os.path.exists(path):
            print(f"🚨 Missing expected directory: {d}")
        else:
            print(f"✅ Found: {d}")

if __name__ == "__main__":
    print("🚀 Nancy_Architect is running...\n")
    check_structure(ROOT_DIR)
    print("\n✅ Done.")
