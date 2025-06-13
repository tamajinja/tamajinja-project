# README.md に logs/index.html へのリンクを追記するマクロ

from pathlib import Path

def append_logs_link_to_readme(readme_path="README.md"):
    readme_file = Path(readme_path)
    content = readme_file.read_text(encoding="utf-8")

    link_block = "\n## 差異ログ一覧（自動生成）\n\n🔗 [logs/index.html](logs/index.html) – 差異ファイル一覧をHTMLで閲覧\n"

    if "logs/index.html" not in content:
        content += link_block
        readme_file.write_text(content, encoding="utf-8")
        print("[INFO] 差異ログリンクをREADME.mdに追記しました")
    else:
        print("[INFO] 差異ログリンクは既に存在します")

# 使用例
# append_logs_link_to_readme()
