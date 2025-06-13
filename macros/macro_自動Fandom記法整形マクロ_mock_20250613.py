import os
from pathlib import Path
import re

LOGS_DIR = "logs"
OUTPUT_SUBDIR = "整形済"
CATEGORY_DEFAULT = "[[Category:分類保留]]"

備考テンプレ = """== 備考 ==
この項目は、**フィクションに基づく設定という“設定”です。**
科学的根拠はありませんが、文化的・民間信仰の枠組みを用いた構成上の意味があります。。

* ▶️ '''[https://www.youtube.com/channel/UCFaSKDRqrRrpGIivzij4GYg YouTubeチャンネル（たま神社 -成仏進行形-）で本編を見る]'''
* 📕 '''[https://note.com/tama_chan_nel note（裏たま）で裏話を読む]'''
* ✴️ '''[https://twitter.com/tama_reikai X（旧Twitter）@tama_reikai（日本語） / @tamashrine（English）]'''
* 📸 '''[https://www.instagram.com/tamashrine Instagram（世界観ビジュアル）]'''
* 🎵 '''[https://www.tiktok.com/@tamachanneltiktok TikTok（オカルト猫ミーム）]'''
* 📚 '''[[用語一覧]] – 五十音順にまとめた事典ページ'''
"""

def fandom整形(md_path: Path, output_dir: Path):
    with md_path.open("r", encoding="utf-8") as f:
        lines = f.readlines()

    result_lines = []
    has_category = False
    has_備考 = False

    for line in lines:
        # 見出し変換
        line = re.sub(r"^#\s*(.+)", r"== \1 ==", line)
        line = re.sub(r"^##\s*(.+)", r"=== \1 ===", line)

        # Markdownリンク除去 or 変換
        line = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"【\1】", line)

        # 強調記法除去
        line = re.sub(r"(\*\*|\*)([^\*]+)(\*\*|\*)", r"\2", line)

        if "[[Category:" in line:
            has_category = True
        if "== 備考 ==" in line:
            has_備考 = True

        result_lines.append(line)

    if not has_備考:
        result_lines.append("\n" + 備考テンプレ + "\n")
    if not has_category:
        result_lines.append(CATEGORY_DEFAULT + "\n")

    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / (md_path.stem + ".fandom.txt")
    output_path.write_text("".join(result_lines), encoding="utf-8")
    print(f"✅ 整形出力: {output_path}")

def main():
    root = Path(LOGS_DIR)
    for category in root.iterdir():
        if category.is_dir():
            output_dir = category / OUTPUT_SUBDIR
            for file in category.glob("*.md"):
                fandom整形(file, output_dir)

if __name__ == "__main__":
    main()
