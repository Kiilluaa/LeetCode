# Given the root of a binary tree, return the number of nodes containing negative values.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_negative_tree_nodes(root):
    def dfs(node):
        if node is None:
            return 0

        check_left = dfs(node.left)
        check_right = dfs(node.right)

        if node.val < 0:
            return 1 + check_left + check_right
        else:
            return check_right + check_left

    return dfs(root)


# Test 1: Multiple negative values
tree1 = TreeNode(-5)
tree1.left = TreeNode(3)
tree1.right = TreeNode(-8)
tree1.left.left = TreeNode(-2)
tree1.left.right = TreeNode(7)
tree1.right.right = TreeNode(-4)
print(count_negative_tree_nodes(tree1))  # Expected: 4


# Test 2: Single negative node
print(count_negative_tree_nodes(TreeNode(-10)))  # Expected: 1


# Test 3: Empty tree
print(count_negative_tree_nodes(None))  # Expected: 0


# Test 4: No negative values
tree4 = TreeNode(0)
tree4.left = TreeNode(5)
tree4.right = TreeNode(10)
print(count_negative_tree_nodes(tree4))  # Expected: 0


# Test 5: All negative values
tree5 = TreeNode(-1)
tree5.left = TreeNode(-2)
tree5.right = TreeNode(-3)
tree5.left.left = TreeNode(-4)
print(count_negative_tree_nodes(tree5))  # Expected: 4


# Test 6: Unbalanced tree
tree6 = TreeNode(10)
tree6.right = TreeNode(-5)
tree6.right.left = TreeNode(3)
tree6.right.left.right = TreeNode(-7)
print(count_negative_tree_nodes(tree6))  # Expected: 2
