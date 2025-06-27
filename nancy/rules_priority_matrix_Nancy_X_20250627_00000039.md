---
type: rule
title: Nancy構造：優先度マトリクスと判断ポリシー
version: v1.0.1
updated: 2025-06-27T01:00:00+0900
file_name: rules_priority_matrix_Nancy_X_20250627_00000039.md
thread_origin: thread_Nancy_X_20250627_00000039
namespace: nancy.rules
scope: meta-definition
status: active
priority: high
tags:
  - Nancy_X
  - rules
  - priority
  - judgment
  - matrix
linked_threads:
  previous: 
  related:
    - id: 
      type: 
      note: 
    - id:
      type: 
      note:
description: >
  このファイルは、Nancy構造群における判断優先度と入力ポリシーを定義したものです。
  `status` や `priority` のような明示的判断をユーザーに求める項目と、`tags`, `notes`, `related` など
  システム側で補完可能な項目を明確に分離しています。
  また、スレッド相互リンクの定義形式と、その運用推奨パターンも併記されています。
---

# Nancy構造：優先度マトリクスと判断ポリシー  
## スレッド: thread_Nancy_X_20250624_00000029

この文書は、Nancy構造群における**優先度の設定ルール**および**ユーザー判断項目の整理基準**を明文化したものです。

---

## ✅ 優先度判断マトリクス

| 項目        | 自動補完 | ユーザー判断 | 補足 |
|-------------|-----------|----------------|------|
| `status`    | ❌        | ✅              | ユーザーの判断が必要なフラグ。例: active, pending, archivedなど。 |
| `priority`  | ❌        | ✅              | スレッド/処理の優先度：low, normal, high, criticalなど。 |
| `tags`      | ⭕        | 任意           | ペルソナ名などがあると便利。未指定でも構造上は可。 |
| `notes`     | ⭕        | 任意           | 必須ではないが、構造判断に役立つメモ情報。 |
| `linked_threads` | ⭕   | 明示が望ましい | スレッドの流れを明示。crosslinkやreference指定に有用。 |
| `related`   | ⭕        | 空配列可       | 構造理解に資する関連ファイル/モジュール。空でも問題なし。 |

---

## 🧩 推奨運用

- `status`, `priority`は**常にユーザーが明示**してください。
- `tags`, `notes`, `related`は**文脈によって補完**可能ですが、構造的な意味を強化したい場合は**手動指定を推奨**。
- `related: []` のような空配列も**記述がある方がGPT補完上は望ましい**です。

---

## 🛠 対象範囲

このポリシーは `nancy/rules/` に属する以下の構造定義に適用されます：

- 優先順位定義（priority）
- ステータス記法（status）
- スレッド相互接続（linked_threads, related）
- 自律進化設定（tagsにおけるペルソナ識別）