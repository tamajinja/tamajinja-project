# README差異ログ反映マクロ（擬似スクリプト例 / Python 3）

import os
from pathlib import Path

def generate_readme(directory_path):
    dir_path = Path(directory_path)
    readme_path = dir_path / "README.md"

    # 差異ログファイルを収集（"差異_" で始まり .md 拡張子）
    diff_files = sorted(
        [f for f in dir_path.glob("差異_*.md") if f.name != "README.md"],
        key=lambda f: f.name,
        reverse=True  # 日付降順（YYYYMMDDが後方にある前提）
    )

    # 差異ログ一覧のMarkdownリンクを生成
    link_lines = [f"- [{f.name}](./{f.name})" for f in diff_files]

    # 差異ログ一覧セクションを生成
    section_header = "## 差異ログ一覧（自動生成）"
    new_section = f"{section_header}

" + "\n".join(link_lines)

    # README更新
    if readme_path.exists():
        with readme_path.open("r", encoding="utf-8") as f:
            content = f.read()
        # 既存セクションがあれば置換、なければ末尾に追加
        if section_header in content:
            before, _, after = content.partition(section_header)
            updated_content = before.strip() + "

" + new_section + "
"
        else:
            updated_content = content.strip() + "

" + new_section + "
"
    else:
        updated_content = new_section + "
"

    # 保存
    with readme_path.open("w", encoding="utf-8") as f:
        f.write(updated_content)

    print(f"[INFO] README updated for: {dir_path}")

# 使用例（ローカル実行想定）
# generate_readme("logs/差異比較")
