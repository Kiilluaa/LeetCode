# Given the root of a binary tree and an integer limit, return:
# - True if every node contains a value strictly less than limit.
# - False if any node contains a value greater than or equal to limit.
# This is a regular binary tree, not necessarily a BST.

class Solution(object):
    def allBelowLimit(self, root, limit):
        if root is None:
            return True

        check_left = self.allBelowLimit(root.left, limit)
        check_right = self.allBelowLimit(root.right, limit)

        if root.val >= limit:
            return False

        return check_right and check_left