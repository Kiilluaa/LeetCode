# Given an undirected, unweighted graph, a starting node start, and an integer k, 
# return the minimum number of edges needed to reach any node whose value is greater than k.
# If start > k, return 0. If no qualifying node is reachable, return -1.

from collections import deque

class Solution(object):
    def shortestToGreater(self, graph, start, k):
        visited = set()
        queue = deque([(start, 0)])
        visited.add(start)

        while queue:
            node, distance = queue.popleft()

            if node > k:
                return distance

            for i in graph[node]:
                if i not in visited:
                    visited.add(i)
                    queue.append((i, distance + 1))

        return -1