#!/bin/bash

# Nancyログ同期スクリプト
# Maintainer: Nancy_Architect
# Updated: 2025-07-03

REPO_DIR="/opt/nancy"
LOG_DIR="$REPO_DIR/logs"
BRANCH="main"

cd $REPO_DIR || exit 1

# 確保
if [ ! -d ".git" ]; then
  echo "Gitリポジトリではありません。終了します。"
  exit 1
fi

# 日時取得
DATE=$(date +"%Y-%m-%d %H:%M:%S")

# ステージング
git add $LOG_DIR

# コミット
git commit -m "chore(logs): sync logs at $DATE" || echo "No changes to commit"

# プッシュ
git push origin $BRANCH
