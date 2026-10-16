# Given an undirected graph, a starting node, and a target value, 
# return True if the target is reachable from the starting node. Otherwise, return False.

from collections import deque

class Solution(object):
    def canReachBFS(self, graph, start, target):
        visited = set()
        queue = deque([start])
        visited.add(start)

        while queue:
            node = queue.popleft()
            if node == target:
                return True

            for i in graph[node]:
                if i not in visited:
                    visited.add(i)
                    queue.append(i)

        return False