class Solution(object):
    def maxValueBST(self, root):
        node = root
        if node is None:
            return None

        if node.right:
            return self.maxValueBST(node.right)
        else:
            return node.val