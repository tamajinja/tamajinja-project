
[Uploading log_intent_extraction_fix---
type: specification
version: v1.1.0
updated: 2025-07-03T09:30:00+09:00
file: nancy/protocols/log_intent_extraction.md
alias: VPSログ意図抽出仕様
maintainer: Nancy_VPS_Engineer
status: draft
tags:
  - vps
  - log
  - intent
  - memory_integration
  - priority_label
  - conflict_check
linked_threads:
  - thread_Nancy_X_20250701_00000049
---

# 🧠 VPSログ → 意図抽出仕様（優先度・矛盾検出対応）

## 概要
Nancy構造におけるVPS上のBot起動・構造変更・監視ログから「意図」を抽出し、記憶ノードに格納するための抽出仕様。

---

## 対象ログ

- Bot起動ログ
- meta整備ログ
- GitHub構造更新ログ
- スレッド名やファイル名の生成記録

---

## 意図抽出ルール

| ログ種別 | 抽出意図カテゴリ | コメント |
|----------|------------------|----------|
| スレッド起動 | structure_update | スレッドに対する構造変更意図 |
| persona生成 | persona_extension | Nancy群拡張意図 |
| meta整備 | meta_consistency | メタ情報の整合性保持意図 |
| output差分 | anomaly_alert | 出力異常検知意図 |

---

## 優先度ラベル付与

抽出された意図には以下の優先度ラベルを付与：
- `Critical`：即時対応が必要な矛盾・逸脱
- `Warning`：潜在的な問題がある提案
- `Info`：通常の運用意図

---

## 矛盾検出クロスチェック

抽出された意図は、Nancy_MetaReviewer / Nancy_Memory_Auditor が検出した矛盾レポートと突き合わせ、重複報告や深刻度を補正。

---

## 出力フォーマット（例）

```yaml
intent_id: "log20250703-002"
source: "Nancy_GitHub"
origin_log: "thread_Nancy_X_20250630_00000045"
category: "structure_update"
content: "新しいNancyペルソナを生成"
timestamp: "2025-07-03T09:25:00+09:00"
priority: "Warning"
linked_modules:
  - nancy/github/
  - nancy/rules/
conflict_check:
  status: "passed"
  details: "No conflicting meta detected"
```

---

## 今後の拡張案

- 意図履歴の時系列可視化
- 自動ラベル学習による優先度精度向上
ed.md…]()
