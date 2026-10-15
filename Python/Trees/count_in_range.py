# Given the root of a binary tree and two integers, low and high, 
# return the number of nodes whose values are between low and high, inclusive.

class Solution(object):
    def countInRange(self, root, low, high):
        if root is None:
            return 0

        left_count = self.countInRange(root.left, low, high)
        right_count = self.countInRange(root.right, low, high)

        count = 0
        if low <= root.val <= high:
            count = 1

        return count + left_count + right_count