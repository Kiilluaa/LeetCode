# Given the root of a binary tree and an integer target, return the number of nodes containing values strictly greater than target.

class Solution(object):
    def countGreater(self, root, target):
        if root is None:
            return 0

        left_count = self.countGreater(root.left, target)
        right_count = self.countGreater(root.right, target)

        count = 0
        if root.val > target:
            count = 1

        return count + left_count + right_count