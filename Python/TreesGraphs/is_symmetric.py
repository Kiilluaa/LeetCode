# Given the root of a binary tree, return True if the tree is symmetric around its center.

class Solution(object):
    def isSymmetric(self, root):

        if root is None:
            return True

        def dfs(left, right):
            if left is None and right is None:
                return True
            elif left is None or right is None:
                return False
            elif left.val != right.val:
                return False

            check_outside = dfs(left.left, right.right)
            check_inside = dfs(right.left, left.right)

            return check_outside and check_inside

        return dfs(root.left, root.right)