from pathlib import Path

# フォルダ内のREADMEを自動生成
for folder in ['assistant', 'user', 'guidelines', 'logs']:
    p = Path(folder)
    if p.exists():
        with open(p / 'README.md', 'w') as f:
            f.write(f"# {folder.capitalize()} Folder\n\nこのフォルダには {folder} 関連ファイルが含まれます。")
