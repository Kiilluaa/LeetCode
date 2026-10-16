# Given the root of a binary tree containing integers, return the sum of all node values.

class Solution(object):
    def sumTree(self, root):
        if root is None:
            return 0

        left_sum = self.sumTree(root.left)
        right_sum = self.sumTree(root.right)

        return root.val + left_sum + right_sum