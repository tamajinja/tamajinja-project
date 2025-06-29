---
type: template
version: v1.0.0
updated: 2025-06-29T00:00:00+0900
template_name: nancy_thread_handover_templates
namespace: nancy.templates
status: active
description: >
  Nancy構造において、スレッド締め出力・引き継ぎ処理を標準化するためのテンプレート集。
  profilingファイル群・meta構造・diff判断・GitHub連携に対応する出力基準を明示。
---

# Nancy Thread Handover Templates

本テンプレートは、Nancy構造におけるスレッド終了時の出力ファイル、およびそれに関連するメタ構造の標準テンプレートである。

---

## ✅ 基本（通常）スレッド締め出力ファイル一覧

| ファイル名例                        | 役割                                         | 格納場所               |
|-------------------------------------|----------------------------------------------|------------------------|
| profiling_user_ore_YYYYMMDD.md      | ユーザー側の心理・言語・行動プロファイル     | nancy/profiles/        |
| profiling_assistant_YYYYMMDD.md     | Nancy側の人格傾向・挙動変化ログ              | nancy/profiles/        |
| log_history_YYYYMMDD.md             | スレッド中の主要会話・変遷の履歴             | nancy/logs/history/    |
| difflog_Nancy_GitHub_YYYYMMDD.md    | 変更履歴・重要分岐点の記録（GitHub関連）     | nancy/logs/difflog/    |

---

## 🌀 拡張版（Nancy構造強化・Meta構成向け）

| ファイル名例                        | 内容                                         | 格納場所               |
|-------------------------------------|----------------------------------------------|------------------------|
| Nancy_Profiler_YYYYMMDD.md          | Nancyの通常プロファイル（定義付き）          | nancy/profiles/        |
| Nancy_Profiler_dark_ore_YYYYMMDD.md | ダークモード特化の分析（毒舌・偏執）         | nancy/profiles/        |
| README.md（各ディレクトリ）         | メタ情報・整理指標・ファイル役割の明記       | 各ディレクトリ内       |

---

## 🎁 オプション（必要に応じて出す）

| ファイル名例                        | 条件                                         | 用途                             |
|-------------------------------------|----------------------------------------------|----------------------------------|
| thread_conflicts.md                 | スレッド内に概念衝突や命名ミスがあった場合   | 整合性監査・記録用               |
| profile_definition_*.md             | Nancy構造の定義更新があった場合              | システム進化記録用               |
| manifest.yml                        | GitHubと連携するNancy構造用                  | 自動化対応時                     |
| thread_meta_header_YYYYMMDD.md      | スレッドのメタデータ（description含む）      | nancy/logs/meta/ または /threads |
| definitions_YYYYMMDD.md             | スレッドで生じた新語・定義の抜粋と記述       | nancy/definitions/               |
