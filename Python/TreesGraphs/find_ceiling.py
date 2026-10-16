# Given the root of a BST and an integer target, return the TreeNode 
# containing the smallest value greater than or equal to target. If no such node exists, return None.

class Solution(object):
    def findCeiling(self, root, target):
        node = root
        if node is None:
            return None

        if node.val == target:
            return node
        elif node.val < target:
            return self.findCeiling(node.right, target)

        candidate = self.findCeiling(node.left, target)

        if candidate is None:
            return node
        else:
            return candidate