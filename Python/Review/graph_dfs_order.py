# Given an undirected graph represented as an adjacency list and a starting node, return a list of all reachable nodes in depth-first search order.
# Explore neighbors in the order they appear in the adjacency list.
# Each node should appear only once in the returned list.


def graph_dfs_order(graph, start):
    if start not in graph:
        return []
    visited = set()
    result = []

    def dfs(node):
        if node in visited:
            return

        visited.add(node)
        result.append(node)

        for neighbor in graph[node]:
            dfs(neighbor)
    dfs(start)
    return result


# Test 1: Graph with a cycle
graph1 = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}
print(graph_dfs_order(graph1, "A"))
# Expected: ["A", "B", "D", "C"]


# Test 2: Simple chain
graph2 = {
    "A": ["B"],
    "B": ["A", "C"],
    "C": ["B", "D"],
    "D": ["C"]
}
print(graph_dfs_order(graph2, "A"))
# Expected: ["A", "B", "C", "D"]


# Test 3: Disconnected graph
graph3 = {
    "A": ["B"],
    "B": ["A"],
    "C": ["D"],
    "D": ["C"]
}
print(graph_dfs_order(graph3, "A"))
# Expected: ["A", "B"]


# Test 4: Single node
graph4 = {"A": []}
print(graph_dfs_order(graph4, "A"))
# Expected: ["A"]


# Test 5: More branches
graph5 = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": [],
    "F": []
}
print(graph_dfs_order(graph5, "A"))
# Expected: ["A", "B", "D", "E", "C", "F"]


# Test 6: Empty graph
print(graph_dfs_order({}, "A"))
# Expected: []
