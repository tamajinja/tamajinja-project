import os

# 命名ルールに従ってファイルをリネームする例（仮）
for filename in os.listdir('.'):
    if filename.startswith('old_'):
        new_name = filename.replace('old_', 'new_')
        os.rename(filename, new_name)
