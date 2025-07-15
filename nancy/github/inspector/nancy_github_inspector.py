#!/usr/bin/env python3

import os

ROOT_DIR = os.path.expanduser("~/tamajinja-project")

def check_readme(directory):
    for root, dirs, files in os.walk(directory):
        if 'README.md' not in files:
            rel_path = os.path.relpath(root, ROOT_DIR)
            print(f"🚨 README.md missing: {rel_path}")

if __name__ == "__main__":
    print("🔍 Checking for missing README.md files...")
    check_readme(ROOT_DIR)
    print("✅ Done.")
