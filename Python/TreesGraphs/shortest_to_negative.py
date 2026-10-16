# Given an undirected, unweighted graph with integer-valued nodes and a starting node, 
# return the minimum number of edges required to reach any negative-valued node.
# If start is negative, return 0. If no negative-valued node is reachable, return -1.

from collections import deque

class Solution(object):
    def shortestToNegative(self, graph, start):
        visited = set()
        queue = deque([(start, 0)])
        visited.add(start)

        while queue:
            node, distance = queue.popleft()

            if node < 0:
                return distance

            for i in graph[node]:
                if i not in visited:
                    visited.add(i)
                    queue.append((i, distance + 1))

        return -1