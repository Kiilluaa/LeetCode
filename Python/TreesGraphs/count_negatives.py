# Given the root of a binary tree, return an integer representing the number of nodes containing negative values.

class Solution(object):
    def countNegative(self, root):
        if root is None:
            return 0

        left_count = self.countNegative(root.left)
        right_count = self.countNegative(root.right)

        count = 0
        if root.val < 0:
            count = 1

        return count + left_count + right_count