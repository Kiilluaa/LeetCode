# Given the root of a binary tree, count how many nodes have a value strictly greater than their parent's value.

class Solution(object):
    def countGreaterThanParent(self, root):
        def dfs(node, parent_val):
            if node is None:
                return 0

            count = 0

            if parent_val is not None and node.val > parent_val:
                count = 1

            left_count = dfs(node.left, node.val)
            right_count = dfs(node.right, node.val)

            return count + left_count + right_count

        return dfs(root, None)