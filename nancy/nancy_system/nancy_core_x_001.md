id: nancy_core_x_001
version: 1.1.0
uuid: 7492e891-fd20-4f55-8dc7-c0de410a4560
description: >
  Nancyシステムを構造定義に基づいて自律起動させる中核ノードファイル。
  ペルソナ構成、命令指針、ユーザープロファイル、ログ、診断レベルなどをここに定義。

boot_nodes:
  primary: nancy_profiler_004
  fallback: ../profiles/nancy_safe_mode.md

linked_profiles:
  - ../nancy_profile.md
  - ../user_profile.md
linked_guidelines:
  - ../nancy_guidelines.md
  - ../meta/safety_filter_v2.md
linked_scripts:
  - ../scripts/nancy_boot.sh
logs:
  boot_log: ../logs/nancy_boot.log
  diagnostics: ../logs/nancy_diag.log
diagnostics:
  enabled: true
  type: checksum
  interval: "12h"
boot_flags:
  dry_run: false
  safe_mode: true
