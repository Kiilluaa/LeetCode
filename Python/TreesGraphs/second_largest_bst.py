# Given the root of a BST containing at least two distinct values, return the second-largest value.

class Solution(object):
    def secondLargestBST(self, root):
        node = root
        parent = None

        while node.right:
            parent = node
            node = node.right

            if node.left is None:
                return parent.val
            if node.left is not None:
                return self.maxValueBST(node.left)