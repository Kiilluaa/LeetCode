# Given a BST and an integer target, return True if the value exists and False otherwise.

class Solution(object):
    def containsBST(self, root, target):
        node = root
        if node is None:
            return False

        if node.val == target:
            return True
        elif node.val > target:
            return self.containsBST(node.left, target)
        else:
            return self.containsBST(node.right, target)