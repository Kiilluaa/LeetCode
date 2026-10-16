# Given an undirected graph represented by an adjacency list and a starting node, 
# return the largest value among all nodes reachable from that starting node.

class Solution(object):
    def findLargestReachable(self, graph, start):
        seen = set()

        def dfs(node):
            if node in seen:
                return

            seen.add(node)

            for i in graph[node]:
                dfs(i)

        dfs(start)
        return max(seen)