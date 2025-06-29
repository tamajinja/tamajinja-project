---
type: rule
version: v1.0.0
updated: 2025-06-29T00:00:00+0900
rule_name: rules_naming_convention
namespace: nancy.rules
status: active
description: >
  Nancy構造内でのファイル命名規則に関する基本ルール。スレッドID・日付・役割を明示し、GitHub連携・自動処理の互換性を保つことを目的とする。
---

# ファイル命名規則（Nancy構造）

## 基本形式

    構成要素_日付_スレッドID.md

- 構成要素：`rules` / `profiling_user_ore` / `log_history` など
- 日付：`YYYYMMDD` 形式
- スレッドID（必要な場合）：`00000043` など

## 命名例

- profiling_user_ore_20250629_00000043.md
- log_history_20250629_00000043.md
- rules_naming_convention_20250629_00000043.md

## 命名上の注意

- ファイル名はすべてスネークケースとし、小文字で統一する
- 日付・スレッドIDは必ず末尾に付ける（時系列並びのため）
- README.mdなどの特例を除き、基本は構成要素ベース命名を優先

---
