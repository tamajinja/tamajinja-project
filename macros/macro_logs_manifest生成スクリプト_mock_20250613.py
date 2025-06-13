# logs_manifest.json 生成スクリプト（擬似版）

import os
import re
import json
from pathlib import Path
from collections import defaultdict

def extract_date(filename):
    match = re.search(r'_(\d{8})\.md$', filename)
    return match.group(1)[:4] + '-' + match.group(1)[4:6] + '-' + match.group(1)[6:] if match else None

def generate_manifest(logs_root="logs"):
    root_path = Path(logs_root)
    manifest = defaultdict(list)

    for folder in root_path.iterdir():
        if folder.is_dir():
            for file in folder.glob("差異_*.md"):
                date = extract_date(file.name)
                manifest[folder.name].append({
                    "file": file.name,
                    "path": str(file.parent),
                    "date": date or "unknown"
                })

    # dict を通常の並び順でダンプ
    manifest_json = json.dumps(dict(manifest), ensure_ascii=False, indent=2)
    output_path = Path("logs_manifest.json")
    output_path.write_text(manifest_json, encoding="utf-8")
    print(f"[INFO] logs_manifest.json generated with {sum(len(v) for v in manifest.values())} items.")

# 使用例
# generate_manifest("logs")
