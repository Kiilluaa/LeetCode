# Given the root of a binary tree, return a list containing the sum of node values at each level, from top to bottom.

from collections import deque

class Solution(object):
    def levelSums(self, root):
        if root is None:
            return []

        queue = deque([root])
        result = []

        while queue:
            level_length = len(queue)
            running_sum = 0

            for _ in range(level_length):
                node = queue.popleft()
                running_sum += node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(running_sum)
            
        return result