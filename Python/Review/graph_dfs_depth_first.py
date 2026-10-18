# Given a graph represented as an adjacency list and a starting node, return a list of all reachable nodes in depth-first search order.
# Explore neighbors in the order they appear in the adjacency list. Each node must appear only once.
# Function: explore_graph_depth_first(graph, start)
# Return: A list of node names.


def explore_graph_depth_first(graph, start):
    if start not in graph:
        return []

    visited = set()
    order = []

    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        order.append(node)

        for neighbor in graph[node]:
            dfs(neighbor)
    dfs(start)
    return order


# Test 1: Graph with cycles
graph1 = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "E"],
    "D": ["B", "E"],
    "E": ["D", "C"]
}
print(explore_graph_depth_first(graph1, "A"))
# Expected: ["A", "B", "D", "E", "C"]


# Test 2: Multiple branches
graph2 = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": [],
    "F": []
}
print(explore_graph_depth_first(graph2, "A"))
# Expected: ["A", "B", "D", "E", "C", "F"]


# Test 3: Disconnected graph
graph3 = {
    "P": ["Q"],
    "Q": ["P"],
    "X": ["Y"],
    "Y": ["X"]
}
print(explore_graph_depth_first(graph3, "X"))
# Expected: ["X", "Y"]


# Test 4: Single node
print(explore_graph_depth_first({"Z": []}, "Z"))
# Expected: ["Z"]


# Test 5: Missing starting node
print(explore_graph_depth_first({}, "A"))
# Expected: []


# Test 6: Starting from a different node
print(explore_graph_depth_first(graph1, "C"))
# Expected: ["C", "A", "B", "D", "E"]
