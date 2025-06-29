# rulesディレクトリ内ルール一覧（2025年6月13日現在）

## 📌 概要
このファイルは `/rules/` 配下に格納されているルール群の一覧です。差異ログ管理やフォーマット整形、自動処理テンプレート等の全体設計を俯瞰できるようにまとめています。

----

## 📄 ルール一覧

### 1. 差異ログ運用関連

- [rules_差異ログ運用ルール_20250613.md](./rules_差異ログ運用ルール_20250613.md)  
　→ 差異ファイルの命名規則・格納ルールを定義

- [rules_logs構造設計_20250613.md](./rules_logs構造設計_20250613.md)  
　→ `/logs/` 内のカテゴリ分類と仮想ディレクトリ構成

- [rules_README自動再生成テンプレート_20250613.md](./rules_README自動再生成テンプレート_20250613.md)  
　→ 差異ファイルを `README.md` に自動反映させる処理テンプレート

----

## 🧭 補足
- 各ルールは将来的にGitHub Actionや自動マクロと連携される前提で構築されています。
- この一覧は今後、追加ルールがあれば随時更新されます。

---

（更新日：2025-06-13）
