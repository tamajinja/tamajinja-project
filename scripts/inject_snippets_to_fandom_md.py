import os
from pathlib import Path

def inject_snippet_if_missing(md_path, template_path, output_path):
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    if "== 備考 ==" in content:
        print(f"[SKIP] {md_path} → 既に備考あり")
        return

    with open(template_path, "r", encoding="utf-8") as f:
        snippet = f.read()

    new_content = content.rstrip() + "\n\n" + snippet

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"[OK] {md_path} → {output_path}")

def main():
    # 設定（必要に応じて修正）
    base_dir = Path(__file__).resolve().parent.parent
    input_dir = base_dir / "fandom"
    output_dir = base_dir / "output"
    template_path = base_dir / "rules/snippet_template_v1.1.md"

    # .md ファイルを走査
    for md_file in input_dir.glob("*.md"):
        output_file = output_dir / md_file.name
        inject_snippet_if_missing(md_file, template_path, output_file)

if __name__ == "__main__":
    main()
