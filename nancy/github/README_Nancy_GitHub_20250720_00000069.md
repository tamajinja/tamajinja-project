---
type: readme
version: v1.0.0
updated: 2025-07-20T00:00:00+09:00
title: Nancy GitHub構造整備ガイド
namespace: nancy.github
category: 構造整備思想
status: active
thread_id: thread_Nancy_X_20250720_00000069
linked_modules:
  - nancy/meta/Nancy_MetaRouter
  - nancy/meta/Nancy_MetaDictionary
  - nancy/profiles/Nancy_Architect
  - nancy/profiles/Nancy_GitHub
description: >
  Nancy構造のGitHub実装・命名整備における思想を記載し、安定性・拡張性を担保するガイド。
---

# 📦 Nancy GitHub構造整備ガイド

このディレクトリは、Nancy構造のGitHub実装・命名整備を担います。  
構造の安定性を維持し、命名ポリシー・meta管理・manifest構造を適用します。

## 🔷 方針
- `.md` ファイル命名とmeta挿入の統一
- `rules/`, `profiles/`, `logs/` との整合性を担保
- README, index, summary_indexの整備
- MetaReviewerの指摘事項を反映

## 📁 サブディレクトリ
- `inspector/` … GitHub構造検査Bot用ファイル
- `logs/` … GitHub関連ログ

## 🧩 実装思想
Nancy_GitHubは、「判断よりも安定した整備」に徹します。  
GitHub構造全体を監視し、整合性を保つ役割を担います。

---
Last updated: 2025-07-20
