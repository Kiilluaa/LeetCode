# Given the root of a binary tree and an integer target, return the sum of all node values strictly greater than target.
# This is a regular binary tree, not a BST, so you must consider both subtrees.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sum_nodes_above_target(root, target):
    def dfs(node, target):
        if node is None:
            return 0

        check_left = dfs(node.left, target)
        check_right = dfs(node.right, target)

        if node.val > target:
            return node.val + check_left + check_right
        else:
            return check_right + check_left

    return dfs(root, target)


# Test 1: Mixed values
tree1 = TreeNode(10)
tree1.left = TreeNode(5)
tree1.right = TreeNode(15)
tree1.left.left = TreeNode(3)
tree1.left.right = TreeNode(8)
tree1.right.left = TreeNode(12)
tree1.right.right = TreeNode(20)
print(sum_nodes_above_target(tree1, 9))  # Expected: 57


# Test 2: No qualifying nodes
print(sum_nodes_above_target(tree1, 25))  # Expected: 0


# Test 3: All nodes qualify
print(sum_nodes_above_target(tree1, 0))  # Expected: 73


# Test 4: Empty tree
print(sum_nodes_above_target(None, 5))  # Expected: 0


# Test 5: Negative values
tree5 = TreeNode(-10)
tree5.left = TreeNode(-3)
tree5.right = TreeNode(4)
tree5.left.right = TreeNode(-7)
print(sum_nodes_above_target(tree5, -8))  # Expected: -6


# Test 6: Values equal to target excluded
tree6 = TreeNode(5)
tree6.left = TreeNode(5)
tree6.right = TreeNode(7)
print(sum_nodes_above_target(tree6, 5))  # Expected: 7
