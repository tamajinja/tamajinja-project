import os
from shutil import copyfile

# パス設定
project_root = os.getcwd()
readme_src = os.path.join(project_root, "rules", "README_統合版_with_snippet_script_20250614.md")
readme_dst = os.path.join(project_root, "README.md")
readme_backup = os.path.join(project_root, "README.old.md")

def update_readme():
    # バックアップ
    if os.path.exists(readme_dst):
        copyfile(readme_dst, readme_backup)
        print(f"バックアップ作成: {readme_backup}")

    # 上書き
    copyfile(readme_src, readme_dst)
    print(f"READMEを更新しました: {readme_dst}")

if __name__ == "__main__":
    update_readme()
