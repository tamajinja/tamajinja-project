# README – Templates ディレクトリ（テンプレート設計）

このディレクトリには、Nancyの各種自動操作や応答出力を支援する**テンプレート定義ファイル**を格納しています。  
主にChatGPTへの出力補助・GitHub運用支援・カテゴリ別の構造提示を目的としています。

---

## 📂 主な構成

| ファイル名 | 用途 | 対象領域 |
|------------|------|----------|
| `Directory actions_README.md` | ディレクトリ操作に関するREADME出力例 | 共通操作系 |
| （今後追加予定） | `category_list_template.md` | カテゴリ別一覧テンプレ | rules/logs等 |
| （今後追加予定） | `response_template.md` | ChatGPT応答テンプレート | Chat操作 |

---

## 🔧 用途別の使い方

- ChatGPTとの連携時に「#TEMPLATE:〜」などの構文で呼び出し可能。
- 出力ファイルの文体統一、構造整備、SEO補助を目的に活用されます。

---

## 🗂️ 関連

- `nancy/rules/` : テンプレ使用ルール
- `nancy/logs/` : 実際の出力ログ
- `nancy/formats/` : 出力形式の定義補助（併用可能）

---

## 📌 補足

このテンプレート群は、**GitHub表示最適化とChatGPT操作効率の双方を目的とした補助構造**です。  
分類に迷った場合は、「出力内容の“形式”」はformats、「“用途の流れ”」はtemplatesへ格納してください。
