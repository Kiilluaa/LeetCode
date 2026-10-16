# Given the root of a binary tree, return True if at least one node contains a negative integer. Otherwise, return False.

class Solution(object):
    def hasNegative(self, root):
        if root is None:
            return False

        check_left = self.hasNegative(root.left)
        check_right = self.hasNegative(root.right)

        if root.val < 0:
            return True

        return check_left or check_right