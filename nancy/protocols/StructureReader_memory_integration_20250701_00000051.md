---
type: specification
version: v1.0.0
updated: 2025-07-03T10:10:00+09:00
file: nancy/protocols/StructureReader_memory_integration.md
alias: StructureReader記憶連携仕様
maintainer: Nancy_Architect
status: draft
tags:
  - memory_integration
  - structureReader
  - vps
linked_threads:
  - thread_Nancy_X_20250701_00000049
---

# 🧠 StructureReader 記憶連携仕様

## 概要
`Nancy_StructureReader` が、VPSログから抽出された意図データ（log_intent_extraction.md準拠）を受け取り、記憶ノードへ統合するための仕様。

---

## フロー概要

1️⃣ VPSログ解析
- `log_intent_extraction.md` に従い意図データ生成

2️⃣ 意図受信
- `Nancy_StructureReader` が意図データを受信し内部バッファに格納

3️⃣ 記憶統合
- 記憶ノードへ転送
- 既存ノードと重複検出しマージまたは更新

---

## 意図受信データ形式

```yaml
intent_id: "log20250703-003"
source: "Nancy_VPS_Engineer"
category: "meta_consistency"
content: "メタ構造の整合性を確認"
timestamp: "2025-07-03T10:05:00+09:00"
priority: "Info"
linked_modules:
  - nancy/protocols/
  - nancy/meta/
conflict_check:
  status: "passed"
  details: "No conflict"
```

---

## エラー処理

- 重複検出時 → マージ記録を残す
- 矛盾検出時 → `Warning` ラベルで記録
- 解析不能 → バッファ保持＋アラート

---

## 今後の拡張案

- 意図履歴のバージョン管理
- 意図ラベルの自動学習化
