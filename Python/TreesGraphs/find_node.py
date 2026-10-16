# Given a BST and an integer target, return the TreeNode containing the target, or None if it doesn't exist.

class Solution(object):
    def findNode(self, root, target):
        node = root

        if node is None:
            return None

        if node.val == target:
            return node
        elif node.val < target:
            return self.findNode(node.right, target)
        else:
            return self.findNode(node.left, target)