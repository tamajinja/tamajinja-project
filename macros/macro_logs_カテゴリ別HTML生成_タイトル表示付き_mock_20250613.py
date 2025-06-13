import os
from pathlib import Path
import re

LOGS_DIR = "logs"

INDEX_TEMPLATE = """<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>{category_name} - Index</title>
</head>
<body>
    <h1>{category_name} 一覧</h1>
    <ul>
        {list_items}
    </ul>
    <hr>
    <a href="../index.html">← logsトップへ戻る</a>
</body>
</html>
"""

def extract_title(file_path: Path):
    try:
        with file_path.open("r", encoding="utf-8") as f:
            for line in f:
                m = re.match(r"(?:^#+\s*|^=+\s*)(.+?)(?:\s*=+)?$", line.strip())
                if m:
                    return m.group(1).strip()
                cm = re.match(r"^#\s*タイトル[:：]\s*(.+)$", line.strip())
                if cm:
                    return cm.group(1).strip()
    except Exception as e:
        return f"(読込失敗) {file_path.name}"
    return f"(無題) {file_path.name}"

def generate_index_html(category_path: Path):
    category_name = category_path.name
    files = sorted(category_path.glob("*.*"))
    list_items = ""

    for file in files:
        if file.name == "index.html":
            continue
        title = extract_title(file)
        list_items += f'<li><a href="{file.name}">{title}</a></li>\n'

    html_content = INDEX_TEMPLATE.format(
        category_name=category_name,
        list_items=list_items
    )

    index_path = category_path / "index.html"
    index_path.write_text(html_content, encoding="utf-8")
    print(f"✅ Generated: {index_path}")

def main():
    root = Path(LOGS_DIR)
    if not root.exists():
        print(f"❌ ディレクトリが存在しません: {LOGS_DIR}")
        return

    for category in root.iterdir():
        if category.is_dir():
            generate_index_html(category)

if __name__ == "__main__":
    main()
