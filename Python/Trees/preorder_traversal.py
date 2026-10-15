# Given the root of a binary tree, return a list of all node values in preorder traversal.

class Solution(object):
    def preorderTraversal(self, root):        
        values = []

        def dfs(node):
            if node is None:
                return
            
            values.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return values