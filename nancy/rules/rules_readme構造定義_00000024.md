---
type: rule
namespace: nancy.rules
scope: README_structure
status: active
priority: high
version: v1.0.0
updated: 2025-06-22
---

# 📘 README構造定義ルール

Nancy構造内における各ディレクトリの`README.md`は、以下の形式と役割を満たすことをルールとする。

## ✅ 必須メタ情報

各READMEの冒頭には以下のYAMLメタタグを付与すること：

```yaml
---
type: core / summary
namespace: nancy.[対象領域]
scope: [user | assistant | rules | logs | all]
status: active
priority: medium
thread_origin: [初出スレッドや時刻]
related_threads: []
linked_files: []
version: v1.0.0
updated: [自動もしくは手動記入]
---
```

## 📁 READMEの分類ルール

| 階層 | ファイル名 | type | scope | 説明 |
|------|------------|------|--------|------|
| `/nancy/profiles/Nancy_GitHub/` | `README.md` | `core` | `all` | Nancy_GitHub全体の宣言的中核 |
| `/nancy/profiles/Nancy_GitHub/xxx/` | `README.md` | `core / summary` | `user` or `assistant` | 各構造の要約と中心役割 |
| `/nancy/rules/` | `README.md` | `core / summary` | `rules` | 運用ルールと自動化定義の中核 |
| `/nancy/logs/` | `README.md` | `summary` | `logs` | ログディレクトリの簡易まとめ |

## 📌 注意点

- `core` はNancy構造の中心をなすファイル。必ずトップ層に1つ配置。
- `summary` は複数可。中間層に配置し、領域ごとの要約とナビゲーションの役割を持つ。
- READMEが複数ある場合でも、`README.md`（汎用）と `README_YYYYMMDD.md`（履歴保存）を併用可。

## 🔧 補足機能連携

- 自動メタ挿入マクロ：`macros/auto_meta_insert.py`
- GitHub Pages対応構造マップ：`index_*.yml`と同期
