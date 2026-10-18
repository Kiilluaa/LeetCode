# Given the root of a binary tree, return its maximum depth.
# The maximum depth is the number of nodes along the longest path from the root to a leaf.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maximum_tree_depth(root):
    def dfs(node):
        if node is None:
            return 0

        check_left = dfs(node.left)
        check_right = dfs(node.right)

        return 1 + max(check_right, check_left)
    return dfs(root)


# Test 1: Uneven tree
tree1 = TreeNode(10)
tree1.left = TreeNode(5)
tree1.right = TreeNode(15)
tree1.left.left = TreeNode(3)
tree1.right.right = TreeNode(20)
tree1.left.left.left = TreeNode(1)
print(maximum_tree_depth(tree1))  # Expected: 4


# Test 2: Single node
print(maximum_tree_depth(TreeNode(8)))  # Expected: 1


# Test 3: Empty tree
print(maximum_tree_depth(None))  # Expected: 0


# Test 4: Balanced tree
tree4 = TreeNode(1)
tree4.left = TreeNode(2, TreeNode(4), TreeNode(5))
tree4.right = TreeNode(3, TreeNode(6), TreeNode(7))
print(maximum_tree_depth(tree4))  # Expected: 3


# Test 5: One-sided tree
tree5 = TreeNode(1)
tree5.right = TreeNode(2)
tree5.right.right = TreeNode(3)
tree5.right.right.right = TreeNode(4)
print(maximum_tree_depth(tree5))  # Expected: 4
