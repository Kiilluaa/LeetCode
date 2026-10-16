# Every value in a node's left subtree must be smaller than that node, and every value in its right subtree must be larger.

class Solution(object):
    def isValidBST(self, root):
        def dfs(node, lower, upper):
            if node is None:
                return True

            if not (lower < node.val < upper):
                return False

            return dfs(node.left, lower, node.val) and dfs(node.right, node.val, upper)
        return dfs(root, float("-inf"), float("inf"))