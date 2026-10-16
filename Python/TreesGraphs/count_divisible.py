# Given the root of a binary tree and an integer k, return the number of nodes whose values are evenly divisible by k.
# You can assume k is always greater than 0.
# This is a regular binary tree, not necessarily a BST.

class Solution(object):
    def countDivisible(self, root, k):
        if root is None:
            return 0

        left_count = self.countDivisible(root.left, k)
        right_count = self.countDivisible(root.right, k)

        count = 0
        if root.val % k == 0:
            count = 1

        return count + left_count + right_count

    