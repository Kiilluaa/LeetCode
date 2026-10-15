class Solution(object):
    def searchBST(self, root, val):
        node = root

        while node is not None:
            if node.val > val:
                node = node.left
            elif node.val < val:
                node = node.right
            else:
                return node

        return None