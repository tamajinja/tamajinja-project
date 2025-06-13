
import pandas as pd
import json

def convert_csv_to_json(csv_path, json_path):
    df = pd.read_csv(csv_path)
    records = df.to_dict(orient="records")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)
    print(f"✅ JSONファイルに変換されました: {json_path}")

# 使用例：
# convert_csv_to_json("logs/fandom_subcategory_log_review.csv", "logs/fandom_subcategory_log_with_approval.json")
