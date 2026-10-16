# Given an undirected, unweighted graph and a starting node, 
# return the minimum number of edges required to reach any even-valued node.
# The starting node counts, so if start is even, return 0.
# If no even-valued node is reachable, return -1.

from collections import deque

class Solution(object):
    def shortestToEven(self, graph, start):
        visited = set()
        queue = deque([(start, 0)])
        visited.add(start)

        while queue:
            node, distance = queue.popleft()

            if node % 2 == 0:
                return distance

            for i in graph[node]:
                if i not in visited:
                    visited.add(i)
                    queue.append((i, distance + 1))

        return -1