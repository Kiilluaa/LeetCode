# Return the number of nodes containing values greater than zero.

class Solution(object):
    def countPositive(self, root):
        if root is None:
            return 0

        left_count = self.countPositive(root.left)
        right_count = self.countPositive(root.right)

        count = 0
        if root.val > 0:
            count = 1

        return count + left_count + right_count