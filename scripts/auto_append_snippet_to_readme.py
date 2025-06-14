import os

# 対象のREADMEとスニペットファイルのパス
README_PATH = "README.md"
SNIPPET_PATH = "README_assets/README_導線追加用_snippet.md"

# 挿入マーカー（必要であれば指定）
INSERT_MARKER = "<!-- AUTO-INSERT-POINT -->"

def append_snippet():
    if not os.path.exists(README_PATH):
        print(f"Error: {README_PATH} not found.")
        return
    if not os.path.exists(SNIPPET_PATH):
        print(f"Error: {SNIPPET_PATH} not found.")
        return

    with open(README_PATH, "r", encoding="utf-8") as f:
        readme_lines = f.readlines()

    with open(SNIPPET_PATH, "r", encoding="utf-8") as f:
        snippet_lines = f.readlines()

    inserted = False
    if INSERT_MARKER in "".join(readme_lines):
        new_lines = []
        for line in readme_lines:
            new_lines.append(line)
            if INSERT_MARKER in line and not inserted:
                new_lines.extend(snippet_lines)
                inserted = True
    else:
        readme_lines.append("\n")  # 念のための改行
        readme_lines.extend(snippet_lines)
        new_lines = readme_lines
        inserted = True

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.writelines(new_lines)

    if inserted:
        print("✅ スニペットが正常に追加されました。")
    else:
        print("⚠️ スニペットの追加に失敗しました。")

if __name__ == "__main__":
    append_snippet()
