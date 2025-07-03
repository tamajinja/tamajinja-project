---
type: protocol
version: v1.0.0
updated: 2025-07-03T10:30:00+09:00
file: nancy/protocols/semantic_update_flow.md
alias: semanticタグ自動更新フロー
maintainer: Nancy_Architect
status: draft
tags:
  - semantic
  - automation
  - integration
linked_threads:
  - thread_Nancy_X_20250701_00000049
---

# 🧭 semantic タグ自動更新フロー

## 概要
Nancy構造内で利用される semantic タグを自動的に集計・検証・更新するためのフロー定義。

---

## フロー概要

1️⃣ **タグ収集**
- Nancy構造内の全 `.md` / `.yaml` ファイルから `tags:` を抽出。

2️⃣ **タグ検証**
- 抽出したタグを既存定義と突き合わせ、無効・重複タグを除去。

3️⃣ **タグ統合**
- 新規タグが発見された場合は summary_index.md に追記。
- 廃止されたタグは summary_index.md から削除（アーカイブに記録）。

4️⃣ **通知**
- 更新結果を記録し、GitHub Actions でプルリクを自動生成。

---

## 実装案

- スクリプト：`update_semantic_tags.py` をGitHubに配置
- トリガー：`cron: nightly` または `on: push`
- 出力先：`summary_index.md`

---

## 今後の拡張案

- semanticタグの優先度スコアリング
- タグ間依存性の検出
- ダッシュボード可視化
