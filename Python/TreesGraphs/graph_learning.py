# adjacency list
graph = {
    "A": ["B", "C"], # graph["A"][0-1]
    "B": ["A", "D"], # graph["B"][0-1]
    "C": ["A", "D"], # graph["C"][0-1]
    "D": ["B", "C"]  # graph["D"][0-1]
}

# A <--> B
# ^      ^
# |      |
# v      v
# C <--> D

# connected node neighbors
graph["A"]       # ["B", "C"]
graph["A"][0]    # "B"

# Undirected graph
# - if A connects to B, B also connects to A

# A <-> B
# Visit A
#  -> Visit B
#       -> Visit A
#             -> Visit B
#                   -> ...

# Without a way to track visited nodes, dfs could continue forever

visited = set() # the solution is set()

visited.add("A") # when we visit node A

visited # {"A"}

# before visiting a node
if node in visited:
    return

