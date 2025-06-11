# 応答メタタグ設計案（Nancy Ver.1.0）

以下のタグを、**記事作成時や長文応答時のヘッダまたはメタセクションに自動記録**する仕様として設計：

```markdown
---
# 応答メタタグ（Nancy Ver.1.0）
author: Nancy (GPT-4)
mode: structured / exploratory / diagnostic / narrative
bias_profile:
  - humor_level: low / medium / high
  - tone: formal / neutral / playful / critical
  - user_alignment: high / medium / low
response_quality: stable / experimental / tentative
based_on: user_directive_v20250611 / internal_guideline_v1.2
timestamp: 2025-06-11T17:22:00+09:00
note: 試験用実装です。将来的にJSON形式やYAML形式での自動出力に移行予定。
---
```

---

## 🔖 説明と用途

| タグ名            | 内容例                             | 説明 |
|-------------------|-------------------------------------|------|
| `author`          | Nancy (GPT-4)                       | 応答生成者（AI名） |
| `mode`            | structured / exploratory など       | 構造的応答か探究的かなどの分類 |
| `bias_profile`    | tone/humor/user_alignment等         | 文体やスタンスの自動評価ラベル |
| `response_quality`| stable / tentative 等               | 応答の信頼性ラベル（自動判定） |
| `based_on`        | 使用したガイドラインやプロファイル | Nancyの思考基準となったファイル情報 |
| `timestamp`       | ISO8601形式                         | 応答生成時の時刻ログ |
| `note`            | 任意                               | 試験実装・特殊対応時の備考 |

---

## 🚧 今後の展望
- `reflections.md`への自動反映オプション
- `nancy_log.yaml`に応答単位で記録し、フィードバック学習
- メタタグから自動要約生成 → `nancy_summary_log.md`構築
