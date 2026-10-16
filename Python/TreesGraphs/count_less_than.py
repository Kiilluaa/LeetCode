# Given a binary tree and an integer target, return the number of nodes whose values are strictly less than target.

class Solution(object):
    def countLessThan(self, root, target):
        if root is None:
            return 0

        left_count = self.countLessThan(root.left, target)
        right_count = self.countLessThan(root.right, target)

        count = 0
        if root.val < target:
            count = 1

        return count + left_count + right_count