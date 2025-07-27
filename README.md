# tamajinja-project

## 📘 概要

このリポジトリは、「たま神社 -成仏進行形-」プロジェクトに関連するFandom記事や、自動整形スクリプト、各種ドキュメントを管理するためのリポジトリです。

## 📖 索引一覧

- 📚 [カテゴリ別ログ索引一覧](nancy/README_assets/README_索引_カテゴリ別一覧.md)  
  └ 設計思想、運用ログ、アラート通知、スクリプト、アーキテクチャなどの構造化リンク集

## ✨ 主要ディレクトリ

- `rules/`：Fandom変換ルールなどのガイドライン
- `scripts/`：記事変換やスニペット挿入の補助スクリプト
- `logs/`：カテゴリ提案ログ・レビュー記録
- `README_assets/`：画像や補助マークダウン
- `fandom/`：記事出力先（予定）

## 🧾 ルール・ガイドライン

Fandom記事のMarkdown変換に関する標準ルールは、以下に記載しています。

📄 [fandom変換ルール v1.1（2025年6月14日版）](rules/fandom変換ルール_v1.1_20250614.md)  
📁 [カテゴリマスタ一覧（category_master.json）](logs/category_master.json)

## 🛠 スクリプト：スニペット自動挿入

指定ディレクトリ内の `.md` 記事に対し、「== 備考 ==」が存在しない場合のみ  
テンプレート（`rules/snippet_template_v1.1.md`）を末尾に自動追記します。

- 入力：`fandom/` ディレクトリ内の `.md` ファイル
- 出力：`output/` に追記済バージョンを生成
- スクリプト：`scripts/inject_snippets_to_fandom_md.py`

```bash
cd scripts
python inject_snippets_to_fandom_md.py
