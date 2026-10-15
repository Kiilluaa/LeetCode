# Given the root of a binary tree, return an integer representing the number of nodes containing even values.

class Solution(object):
    def countEven(self, root):
        if root is None:
            return 0

        left_count = self.countEven(root.left)
        right_count = self.countEven(root.right)

        count = 0
        if root.val % 2 == 0:
            count = 1

        return count + left_count + right_count