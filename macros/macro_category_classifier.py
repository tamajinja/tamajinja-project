
def classify_subcategory_reiteki_kouzou(text):
    # 小カテゴリごとのキーワード辞書
    categories = {
        "構成素粒子": ["霊構子", "霊核", "擬似霊核"],
        "波動・共鳴モデル": ["霊波", "共鳴", "共鳴場", "共鳴不全", "霊波二重モデル", "幽場", "非物質的媒質"],
        "伝播・通信モデル": ["再構成型伝播", "地脈送信", "霊媒通信", "双方向モデル", "反転帰結"],
        "融合・憑依構造": ["擬似融合", "融合", "憑依"],
        "空間構造要素": ["霊道", "霊穴", "地脈", "土地神", "関係性"]
    }

    scores = {cat: 0 for cat in categories}

    for cat, keywords in categories.items():
        for kw in keywords:
            scores[cat] += text.count(kw)

    best_match = max(scores, key=scores.get)
    return best_match if scores[best_match] > 0 else None

# 使用例:
# article_text = "この文章には霊波や共鳴場という概念が含まれます。"
# print(classify_subcategory_reiteki_kouzou(article_text))
