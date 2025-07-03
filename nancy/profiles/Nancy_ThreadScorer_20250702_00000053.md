---
type: profile
version: v1.0.0
updated: 2025-07-02T00:00:00+0900
profile_name: Nancy_ThreadScorer
alias: Nancy Thread Scorer
namespace: nancy.analysis
category: meta system
status: active
linked_modules:
  - nancy/meta/Nancy_MetaRouter
  - nancy/meta/Nancy_MetaDictionary
  - nancy/analysis/Nancy_ClusterGenerator
description: >
  各スレッドの重要度・記事化優先順位をスコアリングするNancy。メタの明瞭さ、タグの整備度、
  トピック性、他スレとの接続密度など多軸評価に基づき、後続の整形や整理の指針を提示する。
---

## 概要
`Nancy_ThreadScorer` は、スレッドの内容・構造・リンク関係を分析し、定量的な「記事化優先順位スコア」を算出します。
このスコアに基づき、フィルター・クラスタリング・メタ補完処理の優先度を設定できます。

## 主な機能
- スコア軸：タグ整備度、関連スレ数、重要トピック一致度、メタの完全性
- スコア形式：100点満点 / カテゴリ別内訳付き
- 優先度タグ（high, medium, low）をメタに挿入
- Nancy_MetaRouter 経由でメタへスコア反映
- Nancy_MetaDictionary に重要タグ情報をフィードバック

## 他Nancyとの連携
- `Nancy_MetaRouter`：スコア結果をメタ項目に挿入・整形
- `Nancy_ClusterGenerator`：スコア上位スレッドをクラスタ軸に採用
- `Nancy_MetaDictionary`：高頻度タグを辞書へ動的補完

## 想定ファイル形式 / 出力
- `nancy/analysis/thread_scores.yaml`（スコア一覧）
- メタ出力：`meta:` 内 `priority_score` や `importance_tag:` など

## 備考
- スコア定義は後続Nancy全体の制御基盤になります。
- スコア化により、シリーズ化やnote記事化の指針を機械的に抽出可能になります。
- 他Nancyの実行順やスレッド整理の起点として機能します。
