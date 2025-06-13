import os
from pathlib import Path
import re
import json

LOGS_DIR = "logs"
OUTPUT_FILE = "link_map.json"

def extract_internal_links(md_path: Path):
    links = set()
    with md_path.open("r", encoding="utf-8") as f:
        content = f.read()
        matches = re.findall(r"'''\[\[(.+?)\]\]'''", content)
        for match in matches:
            links.add(match.strip())
    return list(links)

def build_link_map():
    link_map = {}
    root = Path(LOGS_DIR)
    for category in root.iterdir():
        if category.is_dir():
            for md_file in category.glob("*.md"):
                source = md_file.stem
                targets = extract_internal_links(md_file)
                link_map[source] = targets
    return link_map

def main():
    link_map = build_link_map()
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(link_map, f, indent=2, ensure_ascii=False)
    print(f"✅ リンクマップを生成しました: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
