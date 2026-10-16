from collections import deque

class Solution(object):
    def graphBFS(self, graph, start):
        visited = set() # track visited nodes
        result = [] # initialize the returned list

        queue = deque([start]) # define queue in, set up BFS function
        visited.add(start) # mark starting node as visited

        while queue: # process queue
            node = queue.popleft() # remove next node
            result.append(node) # add node to result

            for i in graph[node]: # loop through neighbors of node
                if i not in visited: # check if neighbor is not in seen
                    visited.add(i) # add to visited
                    queue.append(i) # add to queue

        return result # return final list