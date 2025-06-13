# 📁 カテゴリ分類ログ運用指針（Nancy編集支援室）

## 📌 このディレクトリの目的

この `/logs/` ディレクトリは、Nancy編集支援マクロによって生成される中間ログ・差分記録・分類提案のファイルを保管するための場所です。

主に以下の用途に使用されます：

- カテゴリ分類提案ログの保存
- `.md` ファイルへの追記対象確認
- 差異比較や構文補完の履歴保持
- 手動レビュー・承認用の補助情報

---

## 🧠 現在使用中の主ログ

### ✅ `fandom_subcategory_log_with_approval.json`

| 項目 | 説明 |
|------|------|
| filename | 対象の `.md` ファイル名 |
| subcategory | Nancyが提案した小カテゴリ（`霊的構造/◯◯`） |
| approved | `true` の場合のみ、カテゴリが実際に.mdに追記されます |

---

### 🗂 旧ログ（参考用）

- `fandom_subcategory_log.json`  
  → フラグなしの分類結果のみ。参考用・比較用として保持。

---

## ✅ 運用フロー概要（C案：半自動）

1. `macro_category_classifier.py` により自動分類ログを生成
2. 編集者が `approved: true` を追記し承認
3. `macro_category_inserter.py` にて `.md` 末尾にカテゴリを自動追記

---

## 📎 将来拡張に備えた構想

- カテゴリ辞書：`data/category_keywords.json` などで一元管理
- `.csv` や `.md` 索引ページの自動生成モジュールと連携
- GUIレビューツール（Webダッシュボード）による承認支援

---

このREADMEは Nancy によって自動生成されました。
