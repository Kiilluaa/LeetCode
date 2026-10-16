# Given the root of a binary tree, return the number of nodes that have both a left child and a right child.

class Solution(object):
    def countFullNodes(self, root):
        if root is None:
            return 0

        current_count = 0

        if root.left and root.right:
            current_count = 1
        
        left_count = self.countFullNodes(root.left)
        right_count = self.countFullNodes(root.right)

        return current_count + left_count + right_count