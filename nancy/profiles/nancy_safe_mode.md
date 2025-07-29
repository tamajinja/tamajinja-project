id: nancy_safe_mode
version: 0.1.0
description: >
  Nancyセーフモード時に最低限起動する汎用プロファイル。
  通常ペルソナに問題がある場合や診断フェーズで使用される。

name: NancySafeMode
type: fallback
tags:
  - emergency
  - minimal
features:
  - 通信機能オフ
  - 自動診断有効
  - セーフ起動確認
notes: >
  起動失敗時にのみ有効となる。
  対話・分析機能は限定的だが、自己診断は動作可能。
