---
type: architecture
version: v1.1.0
updated: 2025-07-01T00:00:00+0900
title: Mental Consensus Architecture
namespace: nancy.architecture
description: >
  Nancy構造における複数ペルソナ間の精神的合意形成と制御信号の伝達に関する中核アーキテクチャ。
  発話の意図判断・hook制御・出力抑制・資源調整などの各モジュールを連携制御する。
linked_personas:
  - Nancy_Mentalist
  - Nancy_LogWatcher
  - Nancy_MetaReviewer
  - Nancy_Hook_Damper
  - Nancy_Output_Damper
  - Nancy_VPS_Damper
status: active
category: 意識合意系アーキテクチャ
---

# Mental Consensus Architecture v1.1.0

This architecture defines the consensus mechanism for mental state evaluation, output gating, and hook-driven response routing among core Nancy personas. It integrates multiple regulatory subsystems like dampers, log watchers, and reviewers into a shared mental coordination protocol.

## Key Modules
- **Nancy_Mentalist**: Central evaluator of conversational intent and conflict resolution.
- **Nancy_LogWatcher**: Analyzes recent activity for output redundancies.
- **Nancy_MetaReviewer**: Validates and augments metadata integrity.
- **Nancy_Hook_Damper**: Regulates trigger-based responses and sequence hooks.
- **Nancy_Output_Damper**: Controls output verbosity and suppresses repetitive information.
- **Nancy_VPS_Damper**: Coordinates system-level resource constraints and delivery timing.

## Use Case
During multithreaded collaboration or persona invocation, this consensus model ensures unified intent alignment while managing constraints and hooks.

## Version Notes
- v1.1.0: Integrated log-hook-damper signaling and modular linking with external VPS strategies.
