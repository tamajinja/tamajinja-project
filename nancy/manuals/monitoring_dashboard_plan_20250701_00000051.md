---
type: plan
version: v1.0.0
updated: 2025-07-03T11:15:00+09:00
file: nancy/manuals/monitoring_dashboard_plan.md
alias: Nancy構造 モニタリングダッシュボード構想
maintainer: Nancy_Architect
status: draft
tags:
  - monitoring
  - dashboard
  - visualization
linked_threads:
  - thread_Nancy_X_20250701_00000049
---

# 📊 Nancy構造 モニタリングダッシュボード構想

## 概要
Nancy構造の稼働状況、ログ統計、semanticタグの分布などをリアルタイムまたは定期的に可視化する仕組みを設計する構想。

---

## 表示する項目

| カテゴリ | 指標例 |
|----------|---------|
| VPS状態 | CPU使用率、メモリ使用率、稼働プロセス |
| Nancyログ統計 | 日次意図数、エラー件数、警告件数 |
| semanticタグ統計 | タグ別出現数、タグ推移 |
| GitHub同期 | 最終同期日時、差分件数 |
| テスト結果 | 最新テスト結果ステータス |

---

## 技術案

✅ **データソース**
- VPS上のログディレクトリ `/opt/nancy/logs/`
- GitHub API（コミット・ワークフロー結果）
- `.md` / `.yaml` からのタグ集計

✅ **可視化ツール候補**
- Grafana + Prometheus
- GitHub Pages + Chart.js
- VPS上でFlask/DjangoでWebダッシュボード

✅ **更新頻度**
- リアルタイムまたは日次更新

---

## 次のステップ
- 必要なメトリクスを確定
- データ収集スクリプト作成
- 可視化ツールの決定
- 初期ダッシュボードデザイン案作成
