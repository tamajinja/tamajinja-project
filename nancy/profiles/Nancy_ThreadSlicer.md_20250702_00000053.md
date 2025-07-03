---
type: profile
version: v1.2.0
updated: 2025-07-03T12:00:00+0900
profile_name: Nancy_ThreadSlicer
alias: Nancy ThreadSlicer – 記事分割指揮官
namespace: nancy.profiles
category: スレッド構造制御
status: active
linked_modules:
  - nancy/context/
  - nancy/structure/
  - nancy/meta/
  - nancy/filter/
  - nancy/blogger/
  -nancy/trimmer/
---

# Nancy_ThreadSlicer

## 🧠 概要
Nancy_ThreadSlicerは、1つの長大なスレッドを、意味・構造・文脈に応じて記事化しやすい単位に**分割・再編成**するためのモジュールです。

スレッド内容を無断で削除・意図的に編集するのではなく、**意味単位の「切り出し」**と、**再接続のガイドライン付与**によって、構造と文意を損なわない記事展開を支援します。

---

## 🎯 主な目的

- スレッドの長文構造を、記事単位に分割しやすくする
- Nancy構造における**文脈的な統合判断と系列接続**を明示化
- Blogger変換前段階における記事化構造の「スライス案」を提示

---

## 🔧 動作概要

1. Nancy_ContextReader により意味段落単位でスレッドを区切る候補を抽出
2. Nancy_StructureReader により全体構造とつながりを判定
3. Nancy_MetaRouter から `linked_threads` 情報を取得し、系列を接続
4. Nancy_ThreadScorer のスコアリングを元に、優先分割候補を明示
5. Nancy_ClusterGenerator からシリーズ化補助を受け、記事群を出力構成

---

## 🧩 記事分割の目安

- 原則：1記事 2,500〜3,000字程度で熱量維持
- 原文改変は原則禁止、ただし前後のつなぎ・文意解説は挿入可
- 記事内に Nancy_Bloggerの解説を挿入する場合、装飾コメント形式で可

---

## 🔗 連携構造（分割〜接続〜統合）

| 工程 | 協力Nancy | 内容 |
|------|-----------|------|
| 🔍 **分割** | `Nancy_ContextReader` | 文脈的な切れ目の判定（意味的連続性） |
| 　 | `Nancy_StructureReader` | 構造階層の把握と自然な分割位置の決定 |
| 　 | `Nancy_ThreadScorer` | 分割候補ごとの重要度・記事化スコア算出 |
| 🧩 **接続** | `Nancy_MetaRouter` | 分割後の記事同士を`linked_threads`で接続 |
| 　 | `Nancy_MetaCreator` | 分割された各記事へのメタ付与と整合 |
| 🏗 **統合** | `Nancy_ClusterGenerator` | 同系スレをシリーズ構造へ再統合・再編成 |
| 🧼 **調整** | `Nancy_Trimmer` | 安全性・可読性の観点から各分割記事をフィルタリング |
| 🖋 **最終整形** | `Nancy_Blogger` | 各分割記事への注釈・補足コメント・読者導線の挿入 |

---

## 🔖 今後の拡張

- Nancy_Blogger連携により、記事テンプレートへの自動適用
- 「章」レベルでの分割・統合案も出力する統合モードの導入予定