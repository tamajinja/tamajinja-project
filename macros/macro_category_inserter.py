
import os

def insert_category_from_log(md_dir, log_json_path):
    import json

    with open(log_json_path, 'r', encoding='utf-8') as f:
        log_data = json.load(f)

    for entry in log_data:
        if not entry.get("approved", False):
            continue  # 承認されていないものはスキップ

        filename = entry["filename"]
        subcategory = entry["subcategory"]

        file_path = os.path.join(md_dir, filename)
        if not os.path.exists(file_path):
            print(f"ファイルが見つかりません: {filename}")
            continue

        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # すでに同じカテゴリがある場合はスキップ
        category_line = f"[[Category:霊的構造/{subcategory}]]"
        if category_line in content:
            continue

        # コメント欄の直前に挿入（== 😺 コメント欄について == の前）
        insert_marker = "== 😺 コメント欄について =="
        if insert_marker in content:
            parts = content.split(insert_marker)
            new_content = parts[0].rstrip() + f"
{category_line}

" + insert_marker + parts[1]
        else:
            new_content = content.rstrip() + f"

{category_line}
"

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)

        print(f"{filename} にカテゴリを追加しました → {subcategory}")
