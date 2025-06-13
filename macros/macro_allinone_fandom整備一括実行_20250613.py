import os

# 一括実行対象のマクロファイル名（macros/ ディレクトリ内）
macro_list = [
    "macro_fandom記法構文チェッカー_mock_20250613.py",
    "macro_自動Fandom記法整形マクロ_mock_20250613.py",
    "macro_logs_md2html変換スクリプト_mock_20250613.py",
    "macro_logs_カテゴリ別HTML生成_タイトル表示付き_mock_20250613.py",
    "macro_logs_トップインデックス生成スクリプト_mock_20250613.py",
    "macro_内部リンク抽出マップ生成_mock_20250613.py",
    "macro_link_graph可視化_pyvis版_mock_20250613.py"
]

def main():
    for script in macro_list:
        script_path = os.path.join("macros", script)
        if os.path.exists(script_path):
            print(f"▶️ 実行中: {script}")
            os.system(f"python \"{script_path}\"")
        else:
            print(f"⚠️ スキップ: {script}（見つかりません）")
    print("✅ 全マクロ実行完了！")

if __name__ == "__main__":
    main()
