# Given the root of a binary tree, determine whether it follows the Binary Search Tree ordering rules.
# Every node must be greater than all values in its left subtree and smaller than all values in its right subtree.
# Duplicate values are not allowed.
# Function: is_valid_ordered_tree(root)
# Return: True if the entire tree is a valid BST, otherwise False.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_ordered_tree(root):
    def dfs(node, low, up):
        if node is None:
            return True

        check_left = dfs(node.left, low, node.val)
        check_right = dfs(node.right, node.val, up)

        if node.val >= up or node.val <= low:
            return False
        return check_right and check_left
    return dfs(root, float("-inf"), float("inf"))


# Test 1: Valid BST
tree1 = TreeNode(20)
tree1.left = TreeNode(10)
tree1.right = TreeNode(30)
tree1.left.left = TreeNode(5)
tree1.left.right = TreeNode(15)
tree1.right.left = TreeNode(25)
tree1.right.right = TreeNode(40)

print(is_valid_ordered_tree(tree1))  # Expected: True


# Test 2: Invalid deeper node
tree2 = TreeNode(20)
tree2.left = TreeNode(10)
tree2.right = TreeNode(30)
tree2.right.left = TreeNode(15)

print(is_valid_ordered_tree(tree2))  # Expected: False


# Test 3: Empty tree
print(is_valid_ordered_tree(None))  # Expected: True


# Test 4: Single node
print(is_valid_ordered_tree(TreeNode(7)))  # Expected: True


# Test 5: Duplicate value
tree5 = TreeNode(10)
tree5.left = TreeNode(5)
tree5.right = TreeNode(10)

print(is_valid_ordered_tree(tree5))  # Expected: False


# Test 6: Invalid left subtree
tree6 = TreeNode(50)
tree6.left = TreeNode(25)
tree6.right = TreeNode(75)
tree6.left.right = TreeNode(60)

print(is_valid_ordered_tree(tree6))  # Expected: False


# Test 7: Negative values
tree7 = TreeNode(-5)
tree7.left = TreeNode(-10)
tree7.right = TreeNode(0)
tree7.right.left = TreeNode(-2)

print(is_valid_ordered_tree(tree7))  # Expected: True
