# Given the root of a BST, return the smallest value in the tree.
# Because it is a BST:
# - the minimum value is always found by going left until you cannot go left anymore
# If the tree is empty, return None.

class Solution(object):
    def minValueBST(self, root):
        node = root
        if node is None:
            return None

        if node.left:
            return self.minValueBST(node.left)
        else:
            return node.val