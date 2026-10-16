# Given the root of a BST and a target integer val, return the node containing val.
# If the value doesn't exist, return None.
# Remember that we're returning the actual TreeNode object, not its integer value.

class Solution(object):
    def searchBST(self, root, val):
        def dfs(node):
            if node is None:
                return None
                
            if node.val < val:
                return dfs(node.right)
            elif node.val > val:
                return dfs(node.left)
            elif node.val == val:
                return node
            else:
                return None
        return dfs(root)