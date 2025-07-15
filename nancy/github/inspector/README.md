# Nancy_GitHub Inspector

このディレクトリは、Nancy構造における `Nancy_GitHub` の実行スクリプトと設定を管理します。

## 概要

Nancy_GitHub は GitHub リポジトリの構造監査・整備・命名規則適用を担当する Persona です。

- リポジトリ内のREADMEの有無をチェック
- ファイル命名の一貫性をチェック
- 必要なら修正提案を生成

## 構造

nancy/github/inspector/
├── README.md
├── nancy_github_inspector.py
└── …

## 実行方法

このディレクトリに配置されたスクリプトを VPS 上で実行します。

