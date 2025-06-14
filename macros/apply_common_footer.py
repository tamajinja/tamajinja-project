import os
import argparse

# === 設定 ===
DEFAULT_CATEGORY = "霊的構造"
FOOTER_TEMPLATE_PATH = os.path.join("rules", "common_footer_template_20250614.md")
TARGET_DIR = "rules"

def load_footer_template(category_override=None):
    with open(FOOTER_TEMPLATE_PATH, encoding="utf-8") as f:
        content = f.read()
    if category_override:
        content = replace_category(content, category_override)
    return content

def replace_category(text, category):
    import re
    return re.sub(r"\[\[Category:.*?\]\]", f"[[Category:{category}]]", text)

def has_category_line(text):
    return "[[Category:" in text

def apply_footer_to_file(filepath, footer, force_category=None):
    with open(filepath, encoding="utf-8") as f:
        content = f.read()

    # カテゴリ検出＆処理
    if has_category_line(content):
        if force_category:
            content = replace_category(content, force_category)
        else:
            # 既存カテゴリを維持
            content = content.rsplit("== カテゴリー ==", 1)[0].strip()
            footer = footer  # そのまま追加（footer内に== カテゴリー ==含む）
    else:
        # カテゴリがない場合は footer をそのまま追加
        pass

    # フッター差し込み（== 備考 == 以降を削除してから追加）
    if "== 備考 ==" in content:
        content = content.split("== 備考 ==")[0].rstrip()

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n\n" + footer)

def main(force_category=None):
    footer = load_footer_template(force_category)
    for filename in os.listdir(TARGET_DIR):
        if filename.endswith(".md") and not filename.startswith("README"):
            filepath = os.path.join(TARGET_DIR, filename)
            apply_footer_to_file(filepath, footer, force_category)
            print(f"✅ updated: {filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--force-category", help="強制的にカテゴリを上書きする")
    args = parser.parse_args()
    main(force_category=args.force_category)
