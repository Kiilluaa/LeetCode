# Given the root of a binary tree, return a list of its values in Root → Left → Right order.

class Solution(object):
    def preorderTraversal(self, root):
        tree = []

        def dfs(node):
            if node is None:
                return

            tree.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return tree