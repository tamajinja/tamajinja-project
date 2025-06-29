---
type: rule
version: v1.0.0
updated: 20250629
rule_id: rules_descriptor_comparison_20250629_00000043
namespace: nancy.rules
status: active
linked_profiles:
  - nancy/profiles/Nancy_Descriptor.md
  - nancy/profiles/Nancy_Summarizer.md
  - nancy/profiles/Nancy_Definer.md
  - nancy/profiles/Nancy_Describer.md
description: >
  Description/Summary/Definitionsを複数ペルソナで出力し、比較検証を通じて最適なものを選定するためのルール。
summary: >
  各スレッドにおける記述特化ペルソナの出力比較ルールと、採用判断の記録手順を定める。
definitions:
  - Description: 概要文。スレッドや構造物の目的・構成を簡潔に示す。
  - Summary: 要約文。長文の流れや要点を短縮・集約する。
  - Definitions: 用語や構造を明確に定義する文。
---

# Descriptor比較ルール

## 使用ペルソナ
- Nancy_Descriptor（統合型）
- Nancy_Summarizer（要約特化）
- Nancy_Definer（定義特化）
- Nancy_Describer（表現・描写特化）

## 出力形式
- 各ペルソナ1ブロックずつ出力
- ブロック順序は固定

## 比較観点
- 精度：事実性、誤解のなさ
- 表現：簡潔さ、文体の適合性
- 文脈一致性：スレッドとの合致度

## 採用記録
- 採用案に「✅」マーク
- 採用理由を1行で記録

## 推奨テンプレ
ファイル名例：descriptor_comparison_log_20250629_00000043.md
