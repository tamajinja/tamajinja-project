import json
from pathlib import Path
from pyvis.network import Network

LINK_MAP_FILE = "link_map.json"
OUTPUT_FILE = "link_graph.html"

def load_link_map():
    with open(LINK_MAP_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def generate_network_graph(link_map):
    net = Network(height="800px", width="100%", bgcolor="#ffffff", font_color="black")
    net.force_atlas_2based()

    # ノード追加（すべての記事名・用語）
    nodes = set(link_map.keys())
    for targets in link_map.values():
        nodes.update(targets)

    for node in nodes:
        net.add_node(node, label=node)

    # エッジ追加
    for source, targets in link_map.items():
        for target in targets:
            net.add_edge(source, target)

    return net

def main():
    link_map = load_link_map()
    net = generate_network_graph(link_map)
    net.show(OUTPUT_FILE)
    print(f"✅ リンクグラフを生成しました: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
