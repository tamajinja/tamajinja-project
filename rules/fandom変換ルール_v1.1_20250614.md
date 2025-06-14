# Fandom変換ルール v1.1

以下は、tamajinja-project における Fandom記事変換作業の標準ルールです。  
2025年6月時点の運用方針に基づいて整備されています。

## 🔹 基本原則
- 記事内容は、**1次情報（GitHubなどで提示された.md原文）を正とする**
- **Assistantの内部記憶や過去チャット履歴には依存しない**（一貫性が崩れるため）
- 出力は tamajinja-project の GitHub構成と整合する Markdown形式とする

## 🔹 記事構造ルール
- 見出し：`== 見出し ==` を使用（Fandom記法準拠）
- 内部リンク：`'''[[用語名]]'''`
- 外部リンク・参考リンク：【】で括る
- 備考欄：全記事末尾に「== 備考 ==」を記載（以下の定型文）

### 🧾 備考スニペット（最新版）

== 備考 ==
この記述は、'''フィクションに基づく設定という“設定”です。'''  
科学的根拠はありませんが、文化的・民間信仰の枠組みを用いた構成上の意味があります。  
すべての情報は「たま神社／オカルト猫事典」シリーズの世界観に準じています。

----

== 関連リンク ==
* ▶️ '''[https://www.youtube.com/channel/UCFaSKDRqrRrpGIivzij4GYg YouTubeチャンネル（たま神社 -成仏進行形-）で本編を見る]'''
* 📕 '''[https://note.com/tama_chan_nel note（裏たま）で裏話を読む]'''
* ✴️ '''[https://twitter.com/tama_reikai X（旧Twitter）@tama_reikai（日本語）]'''
* 🌎 '''[https://x.com/TamaShrine X（旧Twitter）@tamashrine（English）]'''
* 📸 '''[https://www.instagram.com/tamashrine Instagram（世界観ビジュアル）]'''
* 🎵 '''[https://www.tiktok.com/@tamachanneltiktok TikTok（オカルト猫ミーム）]'''
* 📚 '''[[用語一覧]] – 五十音順にまとめた事典ページ'''

----

== 😺 コメント欄について ==
このコメント欄は、猫神様が昼寝しながら見守る“観測の間”です🪶  
🌿 感想・発見・供養など、ご自由にお残しください。

👻 ただし「これは公式か？」「うちの霊視ではこうだった！」など、他者の御魂を断定するような発言はお控えください。

🪶 たま神社では、霊も人も、ちょっとずつ成仏中。  
コメントも供養の一部として、やさしく受け止めていただけるとうれしいです。

## 🔹 ファイル出力ルール
- ファイル名：`fandom_タイトル_YYYYMMDD.md`
- カテゴリ表記：文末に `[[Category:◯◯]]` を記載
- 使用カテゴリ例：
  - `[[Category:霊的構造]]`
  - `[[Category:霊的法則]]`
  - `[[Category:波動モデル]]`
  - `[[Category:オカルト社会論]]`

▶️ tamajinjaカテゴリ一覧ページ：https://tamachannel.fandom.com/ja/wiki/用語一覧

## 🔹 運用補足
- 本ルールは v1.1 であり、将来的に運用実態に応じて改訂されます。
- 各記事に適したカテゴリは、`logs/category_master.json` を参照すること。　
