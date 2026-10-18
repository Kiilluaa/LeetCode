# Given a graph represented as an adjacency list and a starting node, return a 
# list containing all nodes reachable from the starting node in depth-first search order.
# Explore neighbors in the order they appear in the adjacency list.
# Each node should appear only once, even if the graph contains cycles.


def visit_graph_nodes(graph, start):
    if start not in graph:
        return []

    visited = set()
    order = []

    def dfs(node):
        if node in visited:
            return

        visited.add(node)
        order.append(node)

        for i in graph[node]:
            dfs(i)

    dfs(start)
    return order


# Test 1: Graph with cycles
graph1 = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B", "E"],
    "E": ["B", "D"],
    "F": ["C"]
}

print(visit_graph_nodes(graph1, "A"))
# Expected: ["A", "B", "D", "E", "C", "F"]


# Test 2: Multiple branches
graph2 = {
    "P": ["Q", "R"],
    "Q": ["S", "T"],
    "R": ["U"],
    "S": [],
    "T": [],
    "U": []
}

print(visit_graph_nodes(graph2, "P"))
# Expected: ["P", "Q", "S", "T", "R", "U"]


# Test 3: Disconnected graph
graph3 = {
    "A": ["B"],
    "B": ["A"],
    "X": ["Y"],
    "Y": ["X"]
}

print(visit_graph_nodes(graph3, "X"))
# Expected: ["X", "Y"]


# Test 4: Single node
print(visit_graph_nodes({"Z": []}, "Z"))
# Expected: ["Z"]


# Test 5: Missing starting node
print(visit_graph_nodes({}, "A"))
# Expected: []


# Test 6: Start from a different node
print(visit_graph_nodes(graph1, "C"))
# Expected: ["C", "A", "B", "D", "E", "F"]


# Test 7: Graph with a cycle
graph7 = {
    "1": ["2"],
    "2": ["3"],
    "3": ["1", "4"],
    "4": ["2"]
}

print(visit_graph_nodes(graph7, "1"))
# Expected: ["1", "2", "3", "4"]
