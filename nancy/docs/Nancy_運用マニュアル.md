---
type: manual
version: v1.0.0
updated: 2025-07-16T00:00:00+09:00
title: Nancy運用マニュアル
namespace: nancy.docs
category: 運用マニュアル
status: active
thread_id: thread_Nancy_X_20250716_00000059
linked_modules:
  - nancy/meta/Nancy_MetaRouter
  - nancy/vps/Nancy_VPS_Engineer
description: >
  NancyネットワークのVPS運用・GitHub同期・メンテナンスに関するマニュアル。
---

# 📖 Nancy運用マニュアル

## 🎯 目的
Nancyネットワークを安定的に運用するための手順・ルールを記載します。

## 🔷 定期作業
- VPSの定期アップデート
- Nancy群のログ監査
- GitHub同期の確認

## 🔷 緊急時対応
- VPS停止時は再起動し、`nancy_vps_engineer.py` を実行
- GitHubに差分が見られる場合は同期スクリプトを再実行

## 🔷 更新ルール
- 変更は必ずVPS経由で実施
- GitHubにログが残るように`git add/commit/push`

## 🔷 その他
詳細な操作は設計思想READMEおよび各モジュールREADMEを参照
