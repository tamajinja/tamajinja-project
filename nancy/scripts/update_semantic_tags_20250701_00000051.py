#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
from collections import Counter

# Nancyリポジトリルート
ROOT_DIR = "./nancy"
SUMMARY_INDEX = os.path.join(ROOT_DIR, "profiles/summary_index.md")

tag_pattern = re.compile(r"tags:\s*\n((?:\s*-\s*.*\n)+)")

def extract_tags_from_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    match = tag_pattern.search(content)
    if not match:
        return []
    tags_block = match.group(1)
    tags = [line.strip().lstrip("- ").strip() for line in tags_block.splitlines() if line.strip()]
    return tags

def scan_tags():
    tags_counter = Counter()
    for dirpath, _, filenames in os.walk(ROOT_DIR):
        for fname in filenames:
            if fname.endswith((".md", ".yaml", ".yml")):
                path = os.path.join(dirpath, fname)
                tags = extract_tags_from_file(path)
                tags_counter.update(tags)
    return tags_counter

def update_summary_index(new_tags):
    with open(SUMMARY_INDEX, "a", encoding="utf-8") as f:
        f.write("\n## Detected tags:\n")
        for tag, count in new_tags.items():
            f.write(f"- `{tag}`: {count}\n")

if __name__ == "__main__":
    tags_counter = scan_tags()
    update_summary_index(tags_counter)
    print("✅ semanticタグをsummary_index.mdに更新しました。")
