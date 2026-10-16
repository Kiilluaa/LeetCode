# Given the root of a binary tree, return the minimum depth.
# Minimum depth is the number of nodes along the shortest path from the root to a leaf node.
# A leaf is a node with no children.

class Solution(object):
    def minDepth(self, root):
        if root is None:
            return 0

        count_left = self.minDepth(root.left)
        count_right = self.minDepth(root.right)

        if root.left is None and root.right is None:
            return 1

        if root.right is None:
            return 1 + count_left

        if root.left is None:
            return 1 + count_right

        return 1 + min(count_left, count_right)