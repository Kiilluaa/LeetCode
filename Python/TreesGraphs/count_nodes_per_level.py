# Given the root of a binary tree, return a list containing the number of nodes at each level, from top to bottom.

from collections import deque

class Solution(object):
    def countNodesPerLevel(self, root):
        if root is None:
            return []

        queue = deque([root])
        result = []

        while queue:
            level_length = len(queue)
            result.append(level_length)

            for _ in range(level_length):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return result