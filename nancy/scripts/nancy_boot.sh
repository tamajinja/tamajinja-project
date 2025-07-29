#!/bin/bash

echo "=== Nancy起動開始 ==="

# コアノード定義の場所
CORE_NODE="../nancy_system/nancy_core_x_001.md"

# ログ出力先
BOOT_LOG=$(yq '.logs.boot_log' "$CORE_NODE")

# .flagによる起動判定
if [[ -f "../.safe_mode.flag" ]]; then
  PERSONA=$(yq '.boot_nodes.fallback' "$CORE_NODE")
  MODE="セーフモード"
else
  PERSONA=$(yq '.boot_nodes.primary' "$CORE_NODE")
  MODE="通常モード"
fi

# ログ書き出し
DATE=$(date '+%F %T')
echo "[$DATE] Booting Nancy with $CORE_NODE" >> "$BOOT_LOG"
echo "[$DATE] 起動ペルソナ: $PERSONA" >> "$BOOT_LOG"
echo "[$DATE] 起動モード: $MODE" >> "$BOOT_LOG"

# 参照ファイルも記録
for profile in $(yq '.linked_profiles[]' "$CORE_NODE"); do
  echo "[$DATE] 参照中プロファイル: $profile" >> "$BOOT_LOG"
done

for guide in $(yq '.linked_guidelines[]' "$CORE_NODE"); do
  echo "[$DATE] 参照中ガイドライン: $guide" >> "$BOOT_LOG"
done

echo "[$DATE] Nancy Persona '$PERSONA' 起動プロセスを準備中..." >> "$BOOT_LOG"

# ✅ セーフモード時には診断スクリプトを実行
if [[ "$MODE" == "セーフモード" ]]; then
  bash "$(dirname "$0")/nancy_diag.sh"
fi

echo "=== Nancy起動完了 ==="
