# Given the root of a binary tree, return the total number of nodes in the tree.

class Solution(object):
    def countNodes(self, root):
        if root is None:
            return 0

        left_count = self.countNodes(root.left)
        right_count = self.countNodes(root.right)

        return 1 + left_count + right_count