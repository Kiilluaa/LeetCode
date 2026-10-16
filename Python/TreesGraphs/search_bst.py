# Given the root of a binary search tree and an integer val, return the TreeNode containing val, or None if it doesn't exist.

class Solution(object):
    def searchBST(self, root, val):
        node = root
        if node is None:
            return None

        if node.val == val:
            return node
        elif node.val < val:
            return self.searchBST(node.right, val)
        else:
            return self.searchBST(node.left, val)
