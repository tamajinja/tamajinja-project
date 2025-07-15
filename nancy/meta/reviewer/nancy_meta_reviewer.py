#!/usr/bin/env python3
import os

ROOT_DIR = os.path.expanduser("~/tamajinja-project")

def check_meta_files():
    print("🔍 Checking for meta files consistency...")
    for root, dirs, files in os.walk(ROOT_DIR):
        for file in files:
            if file.endswith(".md") and "meta" in file.lower():
                print(f"✅ Found meta file: {os.path.join(root, file)}")

if __name__ == "__main__":
    print("🚀 Nancy_MetaReviewer is running...\n")
    check_meta_files()
    print("\n✅ Done.")
