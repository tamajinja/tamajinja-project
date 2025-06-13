import os
from pathlib import Path
import re

LOGS_DIR = "logs"
OUTPUT_SUBDIR = "html"
CSS_LINK = "style.css"  # 任意：同階層または共通パスに配置してください

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <link rel="stylesheet" href="{css}">
</head>
<body>
    <h1>{title}</h1>
    <div class="content">
{body}
    </div>
</body>
</html>
"""

def extract_title_and_convert(md_path: Path):
    title = md_path.stem
    body_lines = []

    with md_path.open("r", encoding="utf-8") as f:
        for line in f:
            if title == md_path.stem:
                # 最初に見つかった # 見出し をタイトルとして使う
                m = re.match(r"^#+\s*(.+)$", line)
                if m:
                    title = m.group(1).strip()

            # 内部リンク '''[[用語名]]''' → <strong><a href="...">用語名</a></strong>
            line = re.sub(r"'''\[\[(.+?)\]\]'''", r"<strong><a href='\1.html'>\1</a></strong>", line)

            # Markdown風な見出しをHTML化（簡易）
            line = re.sub(r"^# (.+)", r"<h1>\1</h1>", line)
            line = re.sub(r"^## (.+)", r"<h2>\1</h2>", line)
            line = re.sub(r"^### (.+)", r"<h3>\1</h3>", line)
            body_lines.append(line)

    return title, "".join(body_lines)

def convert_md_to_html(md_path: Path, output_dir: Path):
    title, body_html = extract_title_and_convert(md_path)
    html_content = HTML_TEMPLATE.format(title=title, body=body_html, css=CSS_LINK)

    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / (md_path.stem + ".html")
    output_path.write_text(html_content, encoding="utf-8")
    print(f"✅ Converted: {output_path}")

def main():
    root = Path(LOGS_DIR)
    for category in root.iterdir():
        if category.is_dir():
            output_dir = category / OUTPUT_SUBDIR
            for file in category.glob("*.md"):
                convert_md_to_html(file, output_dir)

if __name__ == "__main__":
    main()
