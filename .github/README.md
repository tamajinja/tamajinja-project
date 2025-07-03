---
type: directory
version: v1.0.0
updated: 2025-07-03T11:00:00+09:00
directory: .github/
alias: GitHub管理ディレクトリ
maintainer: Nancy_Creator
status: active
tags:
  - github
  - workflows
  - ci_cd
linked_threads:
  - thread_Nancy_X_20250701_00000049
---

# 🗂️ .github/

## 概要
このディレクトリはGitHub専用の管理ディレクトリです。  
リポジトリ運用に関するCI/CDワークフローや設定ファイルを格納します。

---

## 構成

| ファイル/ディレクトリ | 説明 |
|-----------------------|------|
| `.github/workflows/` | GitHub Actions ワークフローファイル群 |
| `update_semantic_tags.yml` | semanticタグ更新ワークフロー定義 |

---

## 注意
このディレクトリ以下のファイルはGitHub側の仕様に従い、自動的に読み込まれます。
Nancy構造本体には含まれませんが、運用上必須です。
