# Given the root of a binary tree, return the number of nodes containing odd integers.
# A negative odd number also counts.

class Solution(object):
    def countOdd(self, root):
        if root is None:
            return 0

        left_count = self.countOdd(root.left)
        right_count = self.countOdd(root.right)

        count = 0
        if root.val % 2 == 1:
            count = 1

        return count + left_count + right_count