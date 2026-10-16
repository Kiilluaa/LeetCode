from collections import deque

class Solution(object):
    def shortestPath(self, graph, start, target):
        visited = set()
        queue = deque([(start, 0)])
        visited.add(start)

        while queue:
            node, distance = queue.popleft()

            if node == target:
                return distance

            for i in graph[node]:
                if i not in visited:
                    visited.add(i)
                    queue.append((i, distance + 1))

        return -1