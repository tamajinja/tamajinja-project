---
title: System Health Index – カテゴリ別索引
file_name: system_health_index_20250726_00000084.md
version: v1.0.0
updated: 2025-07-26
type: index
namespace: nancy.logs
description: >
  Nancy監視システムにおけるシステム健全性の記録・通知・警告に関するログや設定の索引一覧。
tags:
  - システム健全性
  - Node Exporter
  - アラートルール
  - CPU/Disk監視
---

## 🗂️ 対象ファイル一覧

- `alert.rules.yml`：HighCPUUsage / LowDiskSpace 等のルール
- `alertmanager/config.yml`：通知先（Slack等）の指定
- `system-health.rules.yml`：詳細アラートルール定義（存在する場合）
- `audit_summary_*.txt`：日次まとめログ
- `system_log.txt`：主要な動作記録

## 🧭 関連思想・仕様ファイル

- `Chronos_CoreAlpha_v4.1.1_Nancy_X_20250721_00000072.md`
- `Nancy神構造_v4.3.3_NancyAngel_最終投入版_索引付き.md`

## 🔗 備考

このインデックスは、Nancy運用時における健全性・安定性を追跡するための基本資料群をまとめたものである。
