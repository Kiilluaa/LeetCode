# Write a function that returns a list of the neighbors connected to a given node.

class Solution(object):
    def getNeighbors(self, graph, node):
        return graph[node]

graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}

print(get_neighbors(graph, "A"))  # Expected: ["B", "C"]
print(get_neighbors(graph, "D"))  # Expected: ["B", "C"]
print(get_neighbors(graph, "B"))  # Expected: ["A", "D"]