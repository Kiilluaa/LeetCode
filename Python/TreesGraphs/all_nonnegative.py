# Given a binary tree, return True if every node contains a value 
# greater than or equal to 0. Return False if any node contains a negative value.

class Solution(object):
    def allNonnegative(self, root):
        if root is None:
            return True

        check_left = self.allNonnegative(root.left)
        check_right = self.allNonnegative(root.right)

        if root.val < 0:
            return False

        return check_left and check_right