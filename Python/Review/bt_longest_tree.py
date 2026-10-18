# Given the root of a binary tree, return the number of nodes in its longest branch, starting at the root and ending at a leaf.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def longest_tree_branch(root):
    def dfs(node):
        if node is None:
            return 0

        check_left = dfs(node.left)
        check_right = dfs(node.right)

        return 1 + max(check_left, check_right)
    return dfs(root)


# Test 1: Uneven tree
tree1 = TreeNode(8)
tree1.left = TreeNode(4)
tree1.right = TreeNode(12)
tree1.left.left = TreeNode(2)
tree1.right.left = TreeNode(10)
tree1.right.right = TreeNode(14)
tree1.right.left.left = TreeNode(9)
print(longest_tree_branch(tree1))  # Expected: 4


# Test 2: Single node
print(longest_tree_branch(TreeNode(5)))  # Expected: 1


# Test 3: Empty tree
print(longest_tree_branch(None))  # Expected: 0


# Test 4: Both branches equally long
tree4 = TreeNode(1)
tree4.left = TreeNode(2, TreeNode(4))
tree4.right = TreeNode(3, None, TreeNode(5))
print(longest_tree_branch(tree4))  # Expected: 3


# Test 5: One-sided tree
tree5 = TreeNode(1)
tree5.left = TreeNode(2)
tree5.left.left = TreeNode(3)
tree5.left.left.left = TreeNode(4)
tree5.left.left.left.left = TreeNode(5)
print(longest_tree_branch(tree5))  # Expected: 5
