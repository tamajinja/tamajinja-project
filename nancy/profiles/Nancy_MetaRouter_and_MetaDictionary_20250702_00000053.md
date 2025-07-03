---
type: meta-module
version: v1.0.0
updated: 2025-07-02T12:00:00+0900
module_name: Nancy_MetaRouter_and_MetaDictionary
alias: MetaRouter ✕ MetaDictionary 統合モジュール
namespace: nancy.meta
status: active
scope: system
priority: critical

linked_modules:
  - nancy/profiles/Nancy_MetaCreator.md
  - nancy/profiles/Nancy_ThreadScorer.md
  - nancy/profiles/Nancy_ClusterGenerator.md
  - nancy/meta/Nancy_TagDefinitionDictionary.yaml
  - nancy/meta/Nancy_CategoryMap.yaml

summary: >
  本モジュールは、Nancyネットワーク上のスレッドにおけるメタ情報（tags, categories, related_threads, linked_files等）のルーティング・最適化と、タグ・カテゴリの一元管理を目的とする。MetaRouterはMetaLinkerの上位統合制御層として機能し、MetaDictionaryはその制御判断の基準となる辞書ファイル群である。

definitions:
  MetaRouter:
    description: >
      スレッドに付加されたメタ情報（例：tags, related_threads, linked_threads, linked_filesなど）を受け取り、内部基準（定義辞書）と照合し、
      冗長性の排除・整合性の確保・補完を行うルーター型のメタ制御エンジン。
    capabilities:
      - タグの意味的統合（類語・別表記をまとめる）
      - linked_threads の自動系列化（前後スレッド関係の補完）
      - linked_files の存在チェック
      - related_threads の重要度・連関度による並び替え

  MetaDictionary:
    description: >
      Nancy構造全体で使用されるタグ・カテゴリの統一辞書。タグの重複、言い換え、分類のブレを抑える役割を持ち、MetaRouterおよびMetaCreator、Medium、ThreadScorerなど多数のNancyが参照する。
    files:
      - Nancy_TagDefinitionDictionary.yaml
      - Nancy_CategoryMap.yaml

usage: |
  MetaCreator → MetaLinker → Nancy_MetaRouter という流れで処理が行われ、RouterはMetaDictionaryを参照して自動補正とタグ・リンクの再構成を行う。
  また、スレッド群を整理するClusterGeneratorやスコアリングを担うThreadScorerにもメタ出力を共有することで、タグ付けとカテゴリ選定に整合性をもたせる。

example:
  - input_tags: ["情報構造", "メタ構造", "tag分類"]
    auto_categorized: ["構造管理"]
    normalized_tags: ["メタ情報", "タグ分類"]
    suggested_links:
      - thread: thread_Nancy_X_20250624_00000029
        reason: "同一構造ルール定義スレッド"

notes: >
  Nancy_MetaRouter と MetaDictionary は出力せず、他のNancyの内部処理用に使われる後方支援モジュールである。
  人間が直接出力する必要はないが、辞書ファイルの更新管理は慎重に行う。

---