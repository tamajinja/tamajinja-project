# logs/index.html を生成するマクロ（擬似版）

import json
from pathlib import Path

def generate_html_index(manifest_path="logs_manifest.json", output_path="logs/index.html"):
    manifest = json.loads(Path(manifest_path).read_text(encoding="utf-8"))

    html = ['<html><head><meta charset="UTF-8"><title>差異ログ一覧</title></head><body>']
    html.append("<h1>差異ログ一覧</h1>")

    for category, items in manifest.items():
        html.append(f"<h2>{category}</h2>")
        if not items:
            html.append("<p><i>（なし）</i></p>")
            continue
        html.append("<ul>")
        for entry in sorted(items, key=lambda x: x['date'], reverse=True):
            name = entry["file"]
            path = entry["path"]
            date = entry.get("date", "unknown")
            href = f"{path}/{name}"
            html.append(f'<li><a href="{href}">{name}</a>（{date}）</li>')
        html.append("</ul>")

    html.append("</body></html>")
    Path(output_path).write_text("\n".join(html), encoding="utf-8")
    print(f"[INFO] index.html generated at {output_path}")

# 使用例
# generate_html_index()
