# Given an adjacency-list graph and a starting node, return the number of 
# distinct nodes reachable from that starting node, including the starting node itself.

class Solution(object):
    def countReachable(self, graph, start):
        seen = set()


        def dfs(node):
            if node in seen:
                return

            seen.add(node)

            for neighbor in graph[node]:
                dfs(neighbor)

        dfs(start)
        return len(seen)

graph = {
    "A": ["B"],
    "B": ["A", "C"],
    "C": ["B"],
    "D": ["E"],
    "E": ["D"]
}

countReachable(graph, "A")  # 3
countReachable(graph, "D")  # 2
countReachable(graph, "C")  # 3