# Given an undirected graph represented by an adjacency list and a starting node, 
# return the number of distinct even-valued nodes reachable from the starting node, including the starting node if it's even.
# You must use BFS with a queue, not recursive DFS.

from collections import deque

class Solution(object):
    def countReachableEvenBFS(self, graph, start):
        visited = set()
        result = []

        queue = deque([start])
        visited.add(start)

        while queue:
            node = queue.popleft()
            if node % 2 == 0:
                result.append(node)

            for i in graph[node]:
                if i not in visited:
                    visited.add(i)
                    queue.append(i)

        return len(result)