# Given a graph represented as an adjacency list and a starting node, return a list of 
# all nodes reachable from the starting node in depth-first search order.
# Explore neighbors in the order they appear in the adjacency list. Each node should
#  only appear once, even if the graph contains cycles.


def depth_first_nodes(graph, start):
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
    "B": ["A", "D"],
    "C": ["A", "E"],
    "D": ["B", "F"],
    "E": ["C", "F"],
    "F": ["D", "E"]
}

print(depth_first_nodes(graph1, "A"))
# Expected: ["A", "B", "D", "F", "E", "C"]


# Test 2: Multiple branches
graph2 = {
    "P": ["Q", "R"],
    "Q": ["S", "T"],
    "R": ["U", "V"],
    "S": [],
    "T": [],
    "U": [],
    "V": []
}

print(depth_first_nodes(graph2, "P"))
# Expected: ["P", "Q", "S", "T", "R", "U", "V"]


# Test 3: Disconnected graph
graph3 = {
    "A": ["B"],
    "B": ["A"],
    "X": ["Y"],
    "Y": ["X"]
}

print(depth_first_nodes(graph3, "A"))
# Expected: ["A", "B"]


# Test 4: Single node
print(depth_first_nodes({"Z": []}, "Z"))
# Expected: ["Z"]


# Test 5: Missing starting node
print(depth_first_nodes({}, "A"))
# Expected: []


# Test 6: Start from a different node
print(depth_first_nodes(graph1, "E"))
# Expected: ["E", "C", "A", "B", "D", "F"]


# Test 7: Cycle connecting all nodes
graph7 = {
    "1": ["2", "4"],
    "2": ["1", "3"],
    "3": ["2", "4"],
    "4": ["3", "1"]
}

print(depth_first_nodes(graph7, "1"))
# Expected: ["1", "2", "3", "4"]
