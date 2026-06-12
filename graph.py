# graph.py
# Your city map represented as a weighted graph
# Edge weights = safety scores (0.0 = very unsafe, 1.0 = very safe)

city_graph = {
    "Hotel": {
        "Market Square": 0.9,
        "Train Station": 0.6
    },
    "Market Square": {
        "Hotel": 0.9,
        "Cafe District": 0.8,
        "Old Town": 0.7
    },
    "Train Station": {
        "Hotel": 0.6,
        "Old Town": 0.4
    },
    "Cafe District": {
        "Market Square": 0.8,
        "Old Town": 0.85,
        "Night Market": 0.5
    },
    "Old Town": {
        "Market Square": 0.7,
        "Train Station": 0.4,
        "Cafe District": 0.85,
        "Night Market": 0.3
    },
    "Night Market": {
        "Cafe District": 0.5,
        "Old Town": 0.3
    }
}


def find_safest_path(graph, start, end):
    # TODO: Implement Dijkstra's algorithm here
    # Hint: you'll need these three things:
    #   1. A way to track the best known safety score to each node
    #   2. A priority queue to always visit the safest next node
    #   3. A way to remember which node you came from (to reconstruct the path)
    pass


if __name__ == "__main__":
    # Test your algorithm here once you've implemented it
    # Expected: Hotel → Market Square → Cafe District → Old Town → Night Market
    result = find_safest_path(city_graph, "Hotel", "Night Market")
    print(result)
