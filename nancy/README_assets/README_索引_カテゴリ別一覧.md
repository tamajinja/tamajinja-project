---
type: index
version: v1.0.0
updated: 2025-07-26T15:00:00+0900
namespace: nancy.alerting
title: 通知・アラート運用ログ索引
scope: logs
status: active
author: user

tags:
  - prometheus
  - alertmanager
  - slack
  - resolved
  - ops-log
  - alerting

linked_files:
  - file: ../logs/ops/alerting_ops_handdown_20250726_00000084.md
    description: SlackTestAlert 停止の記録ログ
    updated: 2025-07-26T05:36:42+0900
    note: Slack通知の本番構成移行に伴い、テストアラートを停止した手順と結果を記録

notes: >
  本インデックスは、Slack通知構成・Prometheus/Alertmanagerの本番構成に関する運用記録を集約するための索引です。
  `nancy/logs/ops/` 以下の通知関連ログが対象です。
---

## 🔔 通知・アラート関連ログ一覧

| 日付       | タイトル | 内容 |
|------------|----------|------|
| 2025-07-26 | [SlackTestAlert 停止記録](../logs/ops/alerting_ops_handdown_20250726_00000084.md) | Slack通知の本番構成移行に伴う静音化処理の記録。resolved通知含む。 |
