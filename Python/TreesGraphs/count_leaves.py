# A leaf node is a node that has no left or right child.
# Given the root of a binary tree, return the number of leaf nodes, not the total number of nodes.

class Solution(object):
    def countLeaves(self, root):
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1

        left_count = self.countLeaves(root.left)
        right_count = self.countLeaves(root.right)

        return left_count + right_count