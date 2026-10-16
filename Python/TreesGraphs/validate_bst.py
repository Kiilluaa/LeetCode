class Solution(object):
    def isValidBST(self, root):

        def dfs(node, lower, upper):
            if node is None:
                return True

            # Check whether node.val violates either bound.
            if lower is not None and node.val <= lower:
                return False
            if upper is not None and node.val >= upper:
                return False
            # Recursively validate both subtrees.
            left_valid = dfs(node.left, lower, node.val)
            right_valid = dfs(node.right, node.val, upper)

            return left_valid and right_valid

        return dfs(root, None, None)