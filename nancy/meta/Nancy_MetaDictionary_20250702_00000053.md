---
type: profile
version: v1.0.0
updated: 2025-07-02T00:00:00+0900
profile_name: Nancy_MetaDictionary
alias: Nancy Meta Dictionary
namespace: nancy.meta
category: meta system
status: active
linked_modules:
  - nancy/meta/Nancy_MetaRouter
  - nancy/analysis/Nancy_ClusterGenerator
  - nancy/analysis/Nancy_ThreadScorer
description: >
  各スレッドのタグ・カテゴリ分類の中核となる辞書管理Nancy。安定したスレッド系列化、
  メタ自動補完、記事クラスタリングに不可欠な基礎構造を担う。辞書はyaml形式で出力・更新され、
  他Nancyとの連携により動的に進化可能。
---

## 概要
`Nancy_MetaDictionary` は、スレッド処理・記事化構造における「タグ辞書管理」の中核を担うNancyです。
タグの揺らぎを吸収し、共通化・標準化されたメタ処理を支援します。

## 主な機能
- タグ・カテゴリの標準辞書化（別名・表記揺れの吸収）
- yaml形式のタグ辞書ファイル出力（`meta_tags.yaml` など）
- Nancy_ThreadScorer からのタグ重要度の動的反映
- Nancy_ClusterGenerator によるクラスタ辞書の追加提案受付
- Nancy_MetaRouter からの補完要求に応答

## 他Nancyとの連携
- `Nancy_MetaRouter`：メタ補完・タグ並び替え指示元
- `Nancy_ThreadScorer`：使用頻度・重要度をフィードバック
- `Nancy_ClusterGenerator`：シリーズタグ提案などを辞書化

## 想定ファイル形式 / 出力
- `nancy/meta/meta_tags.yaml`：基本タグ辞書
- `nancy/meta/meta_categories.yaml`：カテゴリ辞書（任意）
- `nancy/meta/meta_tag_aliases.yaml`：別名対応表（任意）

## 備考
- MetaRouterやCluster機構の安定稼働に必須の基盤構造です。
- タグ自動補完の精度はこの辞書整備に依存します。
- 初期状態では手動整備が必要ですが、スコア・クラスタと連携して自律補完も可能になります。
