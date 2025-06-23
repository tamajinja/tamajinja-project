---
type: core / summary  
namespace: nancy.github  
scope: assistant  
status: active  
priority: medium  
thread_origin: 20250622T01  
related_threads: []  
linked_files: []  
version: v1.0.0  
updated: 2025-06-22TXX:XX  # ← 実際の更新時刻を自動挿入予定
---

# README: Assistant Core

このディレクトリは、`Nancy_GitHub`プロファイルの中核であり、アシスタント視点での構造定義・機能仕様・実装指針を記述する **Core（中核）領域** です。  
将来的には、ここに蓄積された内容が `summary` に反映されるため、**`core / summary` 両用のメタ情報**として構成しています。

---

## 構成方針

- `core`: アシスタント機能の根幹構造、定義、開発指針を記述
- `summary`: 内容を簡易要約したものを別途生成（自動 or 手動）
- Markdownの先頭に**必ずメタブロック**を記載
- 関連ファイルとのリンク情報は `linked_files` に追記
- `thread_origin` は作成・議論開始スレッドの時刻IDを記録

---

## 内容指針

- Nancyアシスタントの機能定義
- GitHub連携時に必要な権限・制約
- ユーザーからのプロンプト解釈基準
- 出力における安全性・信頼性の設計
- 拡張モジュールとの橋渡し設計

---

## 備考

このファイルは `tamajinja-project/nancy/profiles/Nancy_GitHub/assistant_core/` に格納され、  
Nancyアシスタントの構造進化を支えるための **中核ドキュメント**として管理されます。
