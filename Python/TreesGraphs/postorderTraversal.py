# Given a binary tree, return a list of its values in Left → Right → Root order.

class Solution(object):
    def postorderTraversal(self, root):
        tree = []

        def dfs(node):
            if node is None:
                return
            
            dfs(node.left)
            dfs(node.right)
            tree.append(node.val)

        dfs(root)
        return tree