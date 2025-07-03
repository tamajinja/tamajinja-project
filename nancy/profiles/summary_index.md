---
type: index
version: v1.0.0
updated: 2025-07-03T09:50:00+09:00
file: nancy/profiles/summary_index.md
alias: Nancy構造Semantic Summary Index
maintainer: Nancy_Architect
status: active
tags:
  - semantic
  - index
  - summary
  - nancy_profiles
linked_threads:
  - thread_Nancy_X_20250701_00000049
---

# 🧭 Nancy構造 Semantic Summary Index

## 概要
Nancy構造における全構成要素（ペルソナ・Bot・補助モジュール）のsemanticタグと役割、関連スレッド・ファイルを一元的に可視化します。

---

## Semantic タグマップ

| タグ | 概要 | 関連ファイル・スレッド |
|------|------|-------------------------|
| `monitoring` | 監視・観測系Bot（dog_bot/bird_bot） | nancy/bots/dogs/, nancy/bots/bird/ |
| `suppression` | 抑制系モジュール（damper群） | nancy/dampers/ |
| `notification` | 外部通知・可視化 | bird_bot、nancy/slack_hooks/ |
| `memory_integration` | VPSログから記憶連携 | log_intent_extraction.md, StructureReader_memory_integration.md |
| `semantic` | semanticタグ管理 | summary_index.md |
| `affinity_map` | Nancy相関図 | affinity_map.md |

---

## 主要構造体一覧

| 名称 | タイプ | 役割 | 関連スレッド |
|------|-------|------|--------------|
| Nancy_StructureReader | ペルソナ | 構造判断・統合 | thread_Nancy_X_20250701_00000049 |
| Nancy_VPS_Engineer | ペルソナ | VPS構造適合 | thread_Nancy_X_20250701_00000049 |
| dog_bot群 | Bot群 | 監視・抑制 | thread_Nancy_X_20250701_00000049 |
| bird_bot群 | Bot群 | 実況・透明性 | thread_Nancy_X_20250701_00000049 |
| damper群 | モジュール群 | 出力制御 | thread_Nancy_X_20250701_00000049 |

---

## 今後の拡張案

- semanticタグの自動生成と更新フロー実装
- 相関タグと優先度の階層化
