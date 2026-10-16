# Return an integer representing the number of nodes that have exactly one child (left or right, but not both).

class Solution(object):
    def countSingleChild(self, root):
        if root is None:
            return 0

        node_count = 0
        if root.left and not root.right:
            node_count = 1
        elif root.right and not root.left:
            node_count = 1

        left_count = self.countSingleChild(root.left)
        right_count = self.countSingleChild(root.right)

        return node_count + left_count + right_count