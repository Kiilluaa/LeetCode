# Given an undirected graph represented by an adjacency list and a starting node, 
# return the largest odd number reachable from the starting node, including the starting node itself.
# If no reachable nodes have odd values, return -1.

from collections import deque

class Solution(object):
    def findLargestOddBFS(self, graph, start):
        visited = set()
        odds = []

        queue = deque([start])
        visited.add(start)

        while queue:
            node = queue.popleft()

            if node % 2 == 1:
                odds.append(node)

            for i in graph[node]:
                if i not in visited:
                    visited.add(i)
                    queue.append(i)

        if len(odds) > 0:
            return max(odds)
        return -1