import os
from pathlib import Path

# 拡張子やファイル内容に応じて自動分類
Path("assistant").mkdir(exist_ok=True)
Path("user").mkdir(exist_ok=True)

for file in os.listdir('.'):
    if file.endswith('.md'):
        if 'assistant' in file:
            os.rename(file, f'assistant/{file}')
        elif 'user' in file:
            os.rename(file, f'user/{file}')
