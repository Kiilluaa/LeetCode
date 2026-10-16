# Given the root of a binary tree and an integer target, return:
# - True if at least one node contains target.
# - False if the value doesn't exist anywhere in the tree.

class Solution(object):
    def containsValue(self, root, target):
        if root is None:
            return False
        elif root.val == target:
            return True

        check_left = self.containsValue(root.left, target)
        check_right = self.containsValue(root.right, target)

        return check_left or check_right