---
file_name: monitoring_README_fullguide_20250726.md
version: v1.0
updated: 2025-07-26
type: fullguide
namespace: nancy.monitoring
description: >
  NancyにおけるPrometheus・Alertmanager・Grafana・Log管理の完全統合ガイド。
  各構成の役割・設定・連携方法・ファイル位置を明示。
---

# 📊 Nancy Monitoring System 統合ガイド

## 🎯 目的
Nancy全体を安定運用するための監視構成（Prometheus / Alertmanager / Grafana / Log）の統合ガイド。
構成の意図、設定ファイル、表示UI、通知までを一貫して説明。

---

## 🧱 システム構成

- **Prometheus**：監視データの収集・アラート評価エンジン
- **Node Exporter**：VPS状態のメトリクス取得
- **Alertmanager**：アラート通知の集約と配信（Slack等）
- **Grafana**：可視化とダッシュボード操作
- **ログ構成**：ログ保存パス、ローテーション、インデックス記録

---

## 📁 ファイル構成

### Prometheus
- 設定: `/etc/prometheus/prometheus.yml`
- アラートルール: `/etc/prometheus/alert.rules.yml`
- テスト通知: `/etc/prometheus/rules/test_notification.yml`

### Alertmanager
- 設定: `/etc/alertmanager/config.yml`
- 状態確認: `http://localhost:9093/api/v2/status`
- Slack通知確認: `curl` テスト用スクリプト

### Grafana
- 設定: `/etc/grafana/grafana.ini`
- Web UI: `https://grafana.grafana-tamajinja.com/`
- ダッシュボードインポート済

### ログと索引
- ログ保存: `/nancy/logs/`
- ローテーション設定: `/etc/logrotate.d/vps_watcher`
- 索引:
  - `alerting_index_*.md`
  - `system_health_index_*.md`
  - `grafana_dashboard_index_*.md`
  - `logging_index_README.md`

---

## 🔗 関連ファイル

- `nancy/manuals/README_search_index_entry.md`
- `nancy/manuals/logging_index_README.md`
- `nancy/logs/index/alerting_index_*.md`
- `nancy/logs/index/system_health_index_*.md`
- `nancy/logs/index/grafana_dashboard_index_*.md`

---

## 🧪 テスト・確認Tips

- Slack通知: `curl -XPOST` によるテスト送信
- Alertの firing 状態確認：Prometheus UI or CLI
- Grafanaの見た目や並び順は `編集→保存`で変更可能

---

## ✅ 今後のTODO候補

- log/ ディレクトリへの自動索引スクリプト追加
- cronベースのアラート通知ログ監視スクリプト
- Grafana通知連携との比較レビュー

---
