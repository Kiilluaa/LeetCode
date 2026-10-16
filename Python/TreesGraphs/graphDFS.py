class Solution(object):
    def graphDFS(self, graph, start):
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

graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}