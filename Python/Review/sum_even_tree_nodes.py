# Given the root of a binary tree, return the sum of the values of all nodes containing even numbers.
# An even number is any integer divisible by 2, including zero and negative even numbers.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sum_even_tree_nodes(root):
    def dfs(node):
        if node is None:
            return 0

        check_left = dfs(node.left)
        check_right = dfs(node.right)

        if node.val % 2 == 0:
            return node.val + check_left + check_right
        else:
            return check_right + check_left

    return dfs(root)


# Test 1: Mixed even and odd values
tree1 = TreeNode(10)
tree1.left = TreeNode(5)
tree1.right = TreeNode(8)
tree1.left.left = TreeNode(4)
tree1.left.right = TreeNode(7)
tree1.right.right = TreeNode(6)
print(sum_even_tree_nodes(tree1))  # Expected: 28


# Test 2: Single even node
print(sum_even_tree_nodes(TreeNode(12)))  # Expected: 12


# Test 3: Empty tree
print(sum_even_tree_nodes(None))  # Expected: 0


# Test 4: All odd values
tree4 = TreeNode(3)
tree4.left = TreeNode(5)
tree4.right = TreeNode(7)
print(sum_even_tree_nodes(tree4))  # Expected: 0


# Test 5: Negative even numbers and zero
tree5 = TreeNode(-4)
tree5.left = TreeNode(0)
tree5.right = TreeNode(-6)
tree5.left.left = TreeNode(3)
print(sum_even_tree_nodes(tree5))  # Expected: -10


# Test 6: Unbalanced tree
tree6 = TreeNode(1)
tree6.right = TreeNode(2)
tree6.right.left = TreeNode(4)
tree6.right.left.right = TreeNode(8)
print(sum_even_tree_nodes(tree6))  # Expected: 14
