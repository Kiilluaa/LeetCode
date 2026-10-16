# Given the root of a binary tree, return a list of node values in inorder traversal.

class Solution(object):
    def inorderTraversal(self, root):
        tree = []

        def dfs(node):
            if node is None:
                return

            dfs(node.left)
            tree.append(node.val)
            dfs(node.right)

        dfs(root)
        return tree