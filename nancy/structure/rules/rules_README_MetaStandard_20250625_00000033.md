---
type: rule
version: v1.0.0
updated: 2025-06-25T00:00:00+0900
rule_origin: RULES_Nancy_Naming
namespace: nancy.github.rules
scope: system
status: active
priority: high
author: user

tags:
  - rules
  - readme
  - metadata
  - standardization

applies_to:
  - rules
  - profiling
  - logs
  - notes
  - structure

linked_threads:
  - id: thread_Nancy_X_20250625_00000033.md
    type: decision
    note: "READMEメタ構造標準化の正式決定スレッド"

linked_files: []

notes: >
  各README.mdに対して適用される、Nancy構造のメタ情報設計基準を示す文書。
---

# READMEメタ構造標準ルール（Nancy構造STEP1）

この文書は、Nancy構造内の各README.mdに適用される**type別メタ構造ルール**を定めるものです。

---

## 📘 各typeにおけるメタ構造の定義

| type       | 用途                           | メタ構造       |
|------------|--------------------------------|----------------|
| readme     | トップ構造説明                 | 軽量メタ       |
| difflog    | 差分ログ構造                   | 軽量メタ       |
| observer   | 構造観測ログ                   | 軽量メタ       |
| logmeta    | ログ構造のメタ定義             | 完全メタ       |
| profile    | Nancyの人格・構造定義         | 完全メタ       |
| rule       | 命名・運用ルール               | 完全メタ       |

---

## 🔹 軽量メタ テンプレ（例：readme, observer, difflog）

```yaml
---
type: readme
version: v1.0.0
updated: 2025-06-22T13:00:00+0900
namespace: nancy.github
scope: system
status: active
priority: high
author: user

tags:
  - nancy
  - structure
---
```

---

## 🔷 完全メタ テンプレ（例：rule, profile, logmeta）

```yaml
---
type: rule
version: v1.0.0
updated: 2025-06-22T13:00:00+0900
rule_origin: RULES_Nancy_Naming
namespace: nancy.github.rules
scope: system
status: active
priority: high
author: user

tags:
  - nancy
  - metadata
  - standardization

applies_to:
  - logs
  - profiles
  - rules

linked_threads:
  - id: thread_Nancy_X_20250620_00000021.md
    type: reference
    note: "命名ルールの議論が発生したスレッド"

linked_files: []

notes: >
  Nancy構造におけるメタの記述統一を目的とする。
---
```
