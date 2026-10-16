# Given the root of a binary tree, return True if every node contains a 
# positive integer (greater than zero). Otherwise, return False.

class Solution(object):
    def allPositive(self, root):
        if root is None:
            return True

        check_left = self.allPositive(root.left)
        check_right = self.allPositive(root.right)

        if root.val <= 0:
            return False
        return check_left and check_right