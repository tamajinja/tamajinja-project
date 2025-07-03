---
type: manual
version: v1.0.0
updated: 2025-07-03T11:40:00+09:00
file: nancy/manuals/thread_storage_routine.md
alias: Nancy構造 スレッド格納運用ルーティーン
maintainer: Nancy_Architect
status: draft
tags:
  - thread
  - storage
  - routine
linked_threads:
  - thread_Nancy_X_20250701_00000049
---

# 🗂️ Nancy構造 スレッド格納運用ルーティーン

## 概要
Nancy構造の運用中に発生したスレッドや分割議論を、適切にGitHub上に記録・格納するためのルールを定義する。

---

## 格納ディレクトリ

```
nancy/threads/YYYY/MM/
```

例: `nancy/threads/2025/07/thread_Nancy_X_20250701_00000049.md`

---

## ファイル命名規則

- スレッドIDをファイル名に含める。
  例: `thread_Nancy_X_20250701_00000049.md`
- 分割された子スレッドは末尾に `_01`, `_02` を追加。
  例: `thread_Nancy_X_20250701_00000049_01.md`

---

## メタ情報

各スレッドファイルの冒頭には以下を記載：

```markdown
---
type: thread
id: thread_Nancy_X_20250701_00000049
origin: VPS/GitHub/Local
created: 2025-07-03T11:00:00+09:00
tags:
  - context
  - slice
linked_threads:
  - thread_Nancy_X_20250701_00000049_01
---
```

---

## 処理フロー

1️⃣ **Nancy_ContextReader** が全体文脈を読み込む  
2️⃣ **Nancy_ThreadSlicer** がスレッドを分割する  
3️⃣ **Nancy_StructureReader** が暗黙構造を抽出する  
4️⃣ **Nancy_MetaRouter** がメタ情報・リンクを補完する  
5️⃣ **Nancy_ThreadScorer** がスコアを付与する（任意）  
6️⃣ **Nancy_Blogger** が記事化する（任意）

---

## GitHubへの登録

- ブランチ名にスレッドIDを記載
  例: `feature/thread_Nancy_X_20250701_00000049`
- プルリクエストのタイトルにもスレッドIDを含める

---

## 補足

このルーティーンに従うことで、後からスレッドの経緯や相関関係を容易に追跡可能になる。
