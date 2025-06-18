# README_索引_カテゴリ別一覧.md

このファイルは、「tamajinja-project」内で使用されている各種READMEファイルの分類・設置場所・用途を整理した索引です。  
Nancyルール系・ログ構造系・テンプレート構造の明示を含み、運用効率の最適化とChatGPT側のファイル配置判断を補助する目的で作成されています。

---

## 📁 rules/behavior_guidelines

- **ファイル名**: `behavior_guidelines_README.md`
- **設置場所**: `tamajinja-project/nancy/rules/behavior_guidelines/`
- **目的**: Nancyプロジェクトの行動指針（行為ベースのルール定義）
- **注意**: `README.md`としてリネームして設置推奨（GitHub UI対応）

---

## 📁 logs/

- **ファイル名**: `logs_README.md`
- **設置場所**: `tamajinja-project/nancy/logs/`
- **目的**: Nancyプロジェクト内のログ（行動ログ・OCR出力など）に関する集約的ガイドライン
- **注意**: `README.md`としての機能を持たせてもよいが、UI表示用途ではない

---

## 📁 templates/Directory actions

- **ファイル名**: `Directory actions_README.md`
- **設置場所**: `tamajinja-project/nancy/templates/Directory actions/`
- **目的**: Nancy内でのディレクトリアクション（テンプレートによる自動処理）の整理
- **注意**: 実行時テンプレートと連携する前提。ファイル名一致必須ではない

---

## 📁 logs/format_rules

- **ファイル名**: `log_format_rules_README.md`
- **設置場所**: `tamajinja-project/nancy/logs/format_rules/`
- **目的**: Nancyログの形式統一と記述ルールの明示
- **備考**: OCRログなどの整形用として他セクションからも参照される

---

## 📌 補足事項

- ファイル名が `README_〜` で始まっているものは、UI表示用ではなく**分類・索引用**であることが多いため、明示的な表示目的でない限りこのままで問題ありません。
- Nancy構造におけるREADMEは、**"人間が読む説明書"と"AIが設置判断に使う設計書"の2面性**を持ちます。

---