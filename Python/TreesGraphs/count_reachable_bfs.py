# Given an undirected graph represented by an adjacency list and a starting node, 
# return the number of distinct nodes reachable from that starting node, including the starting node.

from collections import deque

class Solution(object):
    def countReachableBFS(self, graph, start):
        visited = set()

        queue = deque([start])
        visited.add(start)

        while queue:
            node = queue.popleft()

            for i in graph[node]:
                if i not in visited:
                    visited.add(i)
                    queue.append(i)

        return len(visited)