# Given the root of a binary tree, return the number of leaf nodes.
# A leaf node has no left or right child.
# This time, do not use a list, dictionary, or set to collect results. 
# Your function must calculate and return the count using recursion.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_terminal_nodes(root):
    def dfs(node):
        if node is None:
            return 0

        if not node.left and not node.right:
            return 1

        check_left = dfs(node.left)
        check_right = dfs(node.right)

        return check_left + check_right

    return dfs(root)

# Test 1: Multiple leaves
tree1 = TreeNode(10)
tree1.left = TreeNode(5)
tree1.right = TreeNode(15)
tree1.left.left = TreeNode(3)
tree1.left.right = TreeNode(7)
tree1.right.right = TreeNode(20)
print(count_terminal_nodes(tree1))  # Expected: 3


# Test 2: Single node
print(count_terminal_nodes(TreeNode(8)))  # Expected: 1


# Test 3: Empty tree
print(count_terminal_nodes(None))  # Expected: 0


# Test 4: Full tree
tree4 = TreeNode(1)
tree4.left = TreeNode(2, TreeNode(4), TreeNode(5))
tree4.right = TreeNode(3, TreeNode(6), TreeNode(7))
print(count_terminal_nodes(tree4))  # Expected: 4


# Test 5: One-sided tree
tree5 = TreeNode(1)
tree5.right = TreeNode(2)
tree5.right.right = TreeNode(3)
print(count_terminal_nodes(tree5))  # Expected: 1
