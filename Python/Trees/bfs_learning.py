from collections import deque

class Solution(object):
    def levelOrder(self, root):
        if root is None:
            return []

        queue = deque([root])
        result = []

        while queue:
            node = queue.popleft()
            result.append(node.val)

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)

        return result