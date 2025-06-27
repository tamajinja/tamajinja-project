---
type: rule
version: v1.0.0
updated: 2025-06-27T00:00:00+0900
thread_name: thread_Nancy_X_20250627_00000038
thread_origin: thread_Nancy_X_20250627_00000038
namespace: nancy.protocol
scope: user
status: active
priority: high
tags:
  - Nancy_x
  - meta_linkage
  - GitHub_policy
linked_threads: []
linked_files: []
notes: >
  本ルールは、Nancyスレッド運用における前後関係（previous / next）および関連関係（related）の記述ルールを定義する。
  原則として、スレッド原本のアーカイブ以外ではprevious / nextを明示せず、relatedはAI判断で自動挿入可能とする。
  また、ChatGPTの記憶との自動接続は禁止され、ユーザーがスレッド情報一式（zip）を渡した場合や、
  GitHub連携時（APIトークン許可）に限り、relatedの入力が許可される。
  さらに、ユーザーがスレッド名を明示する場合は、その名称を出力ファイルに必ず反映させる。
---

# rules_meta_linkage_policy_20250627_00000038

このルールは、Nancy構造下においてスレッドのメタ構造を適切にリンク・記録するためのポリシーである。

## 🔧 主なポリシー内容

- **previous / nextの指定は、原則スレッド原本アーカイブのみ許可**
  - それ以外は記述しない。
- **relatedはAI判断により付与してよい**
  - ただしChatGPT内部記憶との連携は禁止。
  - 明示的なzip渡し・API連携時に限り許可。
- **ユーザーがスレッド名を宣言した場合は出力ファイルに必ず反映**
  - スレッド名の宣言がない場合、ファイル出力時にAIが確認を行う。

今後、これらのルールを基盤にメタ構造の整備と自動反映を拡張予定。
