# Given the root of a binary tree, return its maximum depth.
# The maximum depth is the number of nodes along the longest path from the root down to a leaf.

class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0

        left_count = self.maxDepth(root.left)
        right_count = self.maxDepth(root.right)

        return 1 + max(left_count, right_count)