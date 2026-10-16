# Given a binary tree and an integer target, return how many nodes 
# contain exactly that value. The tree can contain duplicates.

class Solution(object):
    def countTarget(self, root, target):
        if root is None:
            return 0

        left_count = self.countTarget(root.left, target)
        right_count = self.countTarget(root.right, target)

        count = 0
        if root.val == target:
            count = 1

        return count + left_count + right_count