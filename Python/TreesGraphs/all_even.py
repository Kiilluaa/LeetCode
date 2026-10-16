# Given the root of a binary tree, return True if every node contains an even integer. Otherwise, return False.

class Solution(object):
    def allEven(self, root):
        if root is None:
            return True

        check_left = self.allEven(root.left)
        check_right = self.allEven(root.right)

        if root.val % 2 == 1:
            return False

        return check_left and check_right