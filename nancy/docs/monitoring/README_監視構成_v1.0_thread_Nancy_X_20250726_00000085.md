```markdown
---
title: Nancy監視構成 – README（Slack通知連携付き）
file_name: README_監視構成_v1.0_thread_Nancy_X_20250726_00000085.md
version: v1.0
updated: 2025-07-27T07:07:32+09:00
namespace: nancy.monitoring
type: documentation
thread: thread_Nancy_X_20250726_00000085.md
description: >
  Prometheus, Alertmanager, Node Exporter, Slack通知構成を含むNancy監視インフラの運用構成。
  本番用ルールとSlack通知連携が完了しており、再利用可能な構成として記録。
---

# 📡 Nancy監視構成 – Slack通知連携付き

## ✅ 構成全体の概要

- **監視ツール群**：
  - Prometheus（監視エンジン）
  - Node Exporter（リソース収集）
  - Alertmanager（アラート制御）
  - Grafana（視覚化、今後通知も予定）
- **通知先**：Slack（GoatBot🐐経由）
- **通知形式**：
  - alertnameごとに通知（例：NancyHighCPUUsage）
  - summary/description で状況を表示
  - Bot名とアイコンはSlack側で装飾済み

---

## 📁 アラートルール設定（`/etc/prometheus/alert.rules.yml`）

```yaml
groups:
  - name: system-health
    rules:
      - alert: NancyHighCPUUsage
        expr: 100 - (avg by(instance) (rate(node_cpu_seconds_total{mode="idle"}[1m])) * 100) > 80
        for: 1m
        labels:
          severity: warning
          team: nancy
        annotations:
          summary: "🚨 高CPU使用率 on { $labels.instance }"
          description: "CPU使用率が80%を超えています（1分以上）"

      - alert: NancyLowDiskSpace
        expr: node_filesystem_avail_bytes{mountpoint="/"} < 15000000000
        for: 1m
        labels:
          severity: warning
          team: nancy
        annotations:
          summary: "💾 ディスク空き容量不足 on { $labels.instance }"
          description: "/ の空き容量が15GB未満です"

  - name: instance-down
    rules:
      - alert: NancyInstanceDown
        expr: up == 0
        for: 1m
        labels:
          severity: critical
          team: nancy
        annotations:
          summary: "❌ インスタンス停止: { $labels.instance }"
          description: "Prometheusがこのインスタンスからメトリクスを取得できません"
```

---

## 📨 Alertmanager設定（`/etc/alertmanager/config.yml`）

```yaml
global:
  resolve_timeout: 5m

route:
  receiver: 'slack-notifier'
  group_by: ['alertname']
  group_wait: 10s
  group_interval: 1m
  repeat_interval: 1h

  routes:
    - match:
        alertname: SlackTestAlert
      receiver: 'slack-notifier'

    - match:
        alertname: NancyHighCPUUsage
      receiver: 'slack-notifier'

    - match_re:
        severity: .*
      receiver: 'slack-notifier'

receivers:
  - name: 'slack-notifier'
    slack_configs:
      - send_resolved: true
        channel: '#all-nancy-alerts'
        username: '🐐 GoatBot'
        icon_emoji: ':robot_face:'
        api_url: 'https://hooks.slack.com/services/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'
```

---

## 🧪 Slack通知テスト結果（成功）

```
🐐 GoatBot
[FIRING:1] NancySlackTestAlert (test)
```

---

## 🧠 補足メモ

- firing 確認後、自動で Slack に飛ぶことで通知動作が保証されている。
- 今後の強化候補：
  - メモリ・ロードアベレージ監視追加
  - Grafana通知連携
  - team/severityごとの通知分離
```
