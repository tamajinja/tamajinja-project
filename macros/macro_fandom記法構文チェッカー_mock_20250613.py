import os
from pathlib import Path
import re

LOGS_DIR = "logs"

def check_fandom_syntax(md_path: Path):
    errors = []
    with md_path.open("r", encoding="utf-8") as f:
        content = f.read()

        # 1. タイトル（== 見出し ==）があるか？
        if "==" not in content:
            errors.append("❌ 見出し（== タイトル ==）が見つかりません")

        # 2. 内部リンク '''[[○○]]''' が適切か？
        internal_links = re.findall(r"'''\[\[(.+?)\]\]'''", content)
        for link in internal_links:
            if not re.match(r"^[\wぁ-んァ-ヶ一-龠ー]+$", link):
                errors.append(f"⚠️ 不正な内部リンク形式: {link}")

        # 3. カテゴリ記述があるか？
        if "[[Category:" not in content:
            errors.append("⚠️ カテゴリ指定（[[Category:○○]]）が見つかりません")

        # 4. Markdown記法との混在チェック（例: []() のリンク）
        if re.search(r"\[[^\]]+\]\([^\)]+\)", content):
            errors.append("⚠️ Markdown形式のリンクが混在しています")

    return errors

def scan_all_md_files():
    report = {}
    root = Path(LOGS_DIR)
    for category in root.iterdir():
        if category.is_dir():
            for md_file in category.glob("*.md"):
                errors = check_fandom_syntax(md_file)
                if errors:
                    report[md_file] = errors
    return report

def main():
    report = scan_all_md_files()
    if not report:
        print("✅ すべての.mdファイルはFandom記法的に問題なしです。")
    else:
        for path, errors in report.items():
            print(f"📝 {path}:")
            for err in errors:
                print(f"   {err}")
            print("-" * 40)

if __name__ == "__main__":
    main()
