# Given the root of a binary tree and integers low and high, return True if every 
# node's value is within the inclusive range [low, high]. Otherwise, return False.

class Solution(object):
    def allInRange(self, root, low, high):
        if root is None:
            return True

        check_left = self.allInRange(root.left, low, high)
        check_right = self.allInRange(root.right, low, high)

        if root.val < low or root.val > high:
            return False

        return check_right and check_left