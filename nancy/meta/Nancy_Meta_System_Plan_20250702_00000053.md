---
type: plan
version: v1.1.0
updated: 2025-07-02T12:00:00+0900
plan_name: Nancy_Meta_System_Plan
namespace: nancy.meta
scope: system
status: active
priority: highest

tags:
  - meta
  - router
  - dictionary
  - scoring
  - clustering

linked_files:
  - Nancy_MetaDictionary_20250702_00000053.md
  - Nancy_MetaRouter_20250702_00000053.md
  - Nancy_ThreadScorer_20250702_00000053.md
  - Nancy_Trimmer_20250702_00000053.md
  - Nancy_ClusterGenerator_20250702_00000053.md

notes: >
  Nancy構造のメタ処理系の中核計画。スレッド記事化・優先度評価・構造整理に必要な5機能を中心に構成されており、
  MetaRouterがそれらを統合・調整する役割を果たす。GitHubおよびNote展開において必須構造である。
---

## Nancy メタ拡張構造プラン（v1.1.0 / 2025-07-02）

以下の5つの Nancy を中核とした**メタ情報制御および記事化準備構造**を構築する。

---

### 1. `Nancy_MetaDictionary`
- **目的**：タグ・カテゴリの一元管理
- **理由**：タグ辞書なしでは各スレッドの分岐・系列処理が不安定化しやすい
- **出力形式**：`.yaml`を推奨（例：`meta_tags.yaml`）
- **備考**：Nancy_ThreadScorer や Nancy_ClusterGenerator と連携して動的辞書更新可能に

---

### 2. `Nancy_MetaRouter`
- **目的**：Meta情報の分岐制御と整合性の中枢
- **主な補足機能**：
  - `linked_threads` の整理（重複排除・系列化）
  - `tags` の自動補完・優先順位並べ替え（MetaDictionary参照）
  - `related_threads` を `Nancy_ClusterGenerator` の出力で再構成
  - `linked_files` の存在検査・マッチング（警告付き）
- **上位性**：MetaLinkerを内部で活用しつつ、上位から統制

---

### 3. `Nancy_ThreadScorer`
- **目的**：記事化・公開の優先順位スコアを算出
- **評価軸**：
  - 情報密度（ContextReader支援）
  - 面白さ・読解フック（Blogger支援）
  - 安全性リスク（SafetyFilter支援）
- **形式**：各スレッドに `score:` メタ項目を追記可能に

---

### 4. `Nancy_Trimmer`
- **目的**：記事化前の安全性と可読性の確保
- **主な動作**：
  - 危険情報（ハッキング・クラッキング・個人情報）を削除 or 伏せ字化
  - 簡易注釈の追加（訳注）で解釈補助
  - Bloggerへの変換前の調整フィルター
  - ✅ **フィルター適用前後のdiffログ出力機能**を追加予定（透明性強化）

---

### 5. `Nancy_ClusterGenerator`
- **目的**：類似スレッドをクラスタ化し、シリーズ化・構造化を支援
- **手法案**：
  - タグベース類似性クラスタリング（MetaDictionary使用）
  - スレッド文脈的トピック類似（StructureReader/ContextReader使用）
  - 系列スレッドの流れも検出可能に（MetaRouterと連携）
  - ✅ **シリーズ名・代表タグの自動提案**機能を搭載予定（出力の分類性向上）

---

## 格納ディレクトリ提案
| 区分 | ディレクトリ |
|------|--------------|
| メタ制御系 | `nancy/meta/` |
| 分析・構造系 | `nancy/analysis/` |
| 安全フィルタ系 | `nancy/filter/` |

---

### 次ステップ：
- ✅ `Nancy_MetaRouter_and_MetaDictionary.md`（←基幹ルーター・辞書構造）
- ⏳ 各Nancyの個別定義・調整（`.md`形式 / ペルソナ付き）
- ⏳ `Nancy_ClusterGenerator`と`ThreadScorer`によるスレッド自動分類テスト実行
- ⏳ `Trimmer`による事前フィルター適用検証（diffログ含む）
- ⏳ スコア＆クラスタ結果をMetaRouter経由で統合、出力構造に反映