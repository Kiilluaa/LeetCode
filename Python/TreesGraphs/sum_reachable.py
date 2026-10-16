# Given an undirected graph represented by an adjacency list and a starting node, 
# return the sum of all distinct node values reachable from that starting node, including the starting node.

class Solution(object):
    def sumReachable(self, graph, start):
        seen = set()
        sum = 0

        def dfs(node):
            if node in seen:
                return

            seen.add(node)
            sum += node

            for i in graph[node]:
                dfs(i)
        dfs(start)
        return sum