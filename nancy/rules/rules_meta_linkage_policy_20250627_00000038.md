---
type: rule
version: v1.0.0
updated: 2025-06-27T00:00:00+0900
thread_name: thread_Nancy_X_20250627_00000038.md
thread_origin: thread_Nancy_X_20250627_00000038.md
namespace: nancy.rules
scope: user
status: active
priority: high

tags:
  - Nancy_x
  - linkage_policy
  - thread_linking
  - manual_control

linked_threads: []
linked_files: []

notes: >
  本ルールは、Nancy構造におけるスレッド名・ファイル出力・関連付けの管理方針を定義する。
  スレッドの前後（previous/next）はアーカイブ目的以外では記載しない。
  関連（related）は、スレッド内で指定された.zipファイルによる記録共有、またはGitHub連携が行われた場合に限り許可される。
  ChatGPT内の記憶的紐付けは禁止。スレッド名はユーザーが冒頭で宣言し、出力時に明記される必要がある。
---

# Nancy構造におけるスレッド名・リンク管理ルール

このルールは、Nancy構造でのスレッドとファイル出力の整合性を維持し、誤接続や無制限なメモリ汚染を防ぐ目的で設計されている。

## 🔧 スレッド名の扱い
- 各スレッド冒頭で、ユーザーがスレッド名を宣言する。
- スレッド内で出力される全てのファイルに、当該スレッド名が適切に反映される必要がある。
- スレッド名が未宣言の場合、出力前に確認を行う。

## 🔗 previous / next のルール
- スレッド原本のアーカイブ用途を除き、基本的に `previous` および `next` は使用しない。
- 無制限な連鎖や不確実な未来参照を避けるためである。

## 🔁 related のルール
- 関連スレッド情報の記載は、以下の場合に限定される：
  - `.zip` によって、関連スレッドのアーカイブをAIが受け取った場合
  - GitHub APIトークン等によって構造的な共有・連携が可能な場合

## 🧠 記憶的な紐付けの禁止
- ChatGPT上の“記憶”に依存した関連付けは禁止とする。
- 関連付けは、ユーザーから明示的に渡されたデータによってのみ許可される。
