#!/usr/bin/env python3

import yaml
import sys
import time

CONFIG = "consensus_weights.yaml"

def load_config():
    with open(CONFIG, 'r') as f:
        return yaml.safe_load(f)

def collect_votes():
    # ダミーデータ（実運用では実際のBot応答と置き換え）
    return {
        'Nancy_Architect': 'approve',
        'Nancy_VPS_Engineer': 'approve',
        'Nancy_GitHub': 'reject',
        'BirdBot_GitHub_Inspector': 'approve',
        'BirdBot_VPS_Inspector': 'approve',
        'DogBot_Guard': 'reject',
    }

def calculate_consensus(votes, weights):
    score = {}
    for bot, vote in votes.items():
        weight = weights.get(bot, 1)
        score[vote] = score.get(vote, 0) + weight
    return max(score.items(), key=lambda x: x[1])

def main():
    config = load_config()
    weights = config['weights']
    fallback = config['fallback_decider']

    print("⏳ 投票を集計中…")
    start = time.time()
    votes = collect_votes()
    elapsed = time.time() - start

    if elapsed > config['timeout_seconds']:
        print(f"⚠️ タイムアウト。{fallback} に決定権を委譲します。")
        sys.exit(0)

    decision, score = calculate_consensus(votes, weights)
    print(f"✅ Consensus決定: {decision}（スコア: {score}）")

if __name__ == "__main__":
    main()

