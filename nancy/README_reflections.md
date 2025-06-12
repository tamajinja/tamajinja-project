# 🧠 Nancy反省ログ運用ルール（v20250611）

このプロジェクトでは、AI擬似人格Nancyが行った応答に対する「失敗・改善・構造的見直し」を記録・反映するためのログファイルを以下の方針で運用しています。

---

## ✅ 運用構造

```
tamajinja-project/
└── nancy/
    ├── reflections.md                  ← Nancy反省ログの本体（全記録を一元管理）
    ├── logs/
    │   └── reflections_updated_YYYYMMDD.md ← 差分・一時追記ファイル（後で統合）
```

---

## 📄 reflections.md

- Nancyがミスした応答例・理由・改善策を記録
- 全エントリは `## 🧠 Reflection Entry - 日時` で区切り
- Markdownとして手動記録またはテンプレから追記

---

## 🗂 logs/reflections_updated_*.md

- その日の差分ログやドラフトを保管
- 内容を `reflections.md` にマージしたら削除 or アーカイブ

---

## 📌 推奨運用手順

1. 新しいミスや改善点があったら、まず `logs/reflections_updated_YYYYMMDD.md` にテンプレで作成
2. 内容が確定したら `reflections.md` に追記し、差分ファイルは削除またはそのまま保管
3. 日付・内容・改善方針が明示されていること

---

## 🔁 追記テンプレはこちら：
- `/nancy/templates/reflections_template.v20250611.md`

---

## 📬 備考
この仕組みはNancyの再現性・改善学習・スタイル制御のためのメタ構造です。
今後、応答テンプレや挙動モードと連携し、Nancy全体の構造化知能として発展させます。
