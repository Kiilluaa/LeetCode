# Given an undirected graph represented by an adjacency list, a starting node start, and an integer k, 
# return the number of distinct reachable nodes whose values are greater than k.

from collections import deque

class Solution(object):
    def countGreaterBFS(self, graph, start, k):
        visited = set()
        valid = set()

        queue = deque([start])
        visited.add(start)

        while queue:
            node = queue.popleft()

            if node > k:
                valid.add(node)

            for i in graph[node]:
                if i not in visited:
                    visited.add(i)
                    queue.append(i)

        return len(valid)