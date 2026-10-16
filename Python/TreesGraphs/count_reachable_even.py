# Given an undirected graph represented by an adjacency list and a starting node, 
# return the number of distinct reachable nodes whose values are even.

class Solution(object):
    def countReachableEven(self, graph, start):
        seen = set()
        is_even = []

        def dfs(node):
            if node in seen:
                return

            seen.add(node)
            if node % 2 == 0:
                is_even.append(node)

            for i in graph[node]:
                dfs(i)

        dfs(start)
        return len(is_even)