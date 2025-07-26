---
type: index
version: v1.0.0
updated: 2025-07-26T16:00:00+0900
namespace: nancy.prometheus.rules
title: Prometheus アラートルール一覧
scope: rules
status: active
author: user

tags:
  - prometheus
  - alerting
  - rules
  - monitoring
  - index

linked_files:
  - file: ../rules/alert.rules.yml
    description: メインのアラートルール
    updated: 2025-07-25T18:00:00+0900
    note: CPU/Disk/Instanceの死活監視ルールを定義

  - file: ../rules/test_notification.yml
    description: テストアラート専用ルール
    updated: 2025-07-25T18:10:00+0900
    note: Slack連携のテスト送信アラート（AlwaysFiring）

notes: >
  本ファイルは、Prometheusのルール定義を一覧化した索引です。
  本番運用ルールとテスト用ルールの両方を整理してあります。
---

## 📋 アラートルール一覧

| ファイル名 | 説明 | 最終更新 |
|------------|------|----------|
| [alert.rules.yml](../rules/alert.rules.yml) | メインアラートルール（CPU/Disk/Down） | 2025-07-25 |
| [test_notification.yml](../rules/test_notification.yml) | Slack通知テスト用ルール | 2025-07-25 |
