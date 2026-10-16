# Given the roots of two binary trees, p and q, return True if they are identical and False otherwise.
# Two trees are identical when they have exactly the same structure and the same value at every corresponding node.

class Solution(object):
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        elif p.val != q.val:
            return False

        check_left = self.isSameTree(p.left, q.left)
        check_right = self.isSameTree(p.right, q.right)

        if check_left and check_right:
            return True
        else:
            return False