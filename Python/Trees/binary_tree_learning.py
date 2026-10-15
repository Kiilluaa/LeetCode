class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(
    10,
    TreeNode(5),
    TreeNode(15)
)

def count_nodes(root):
    if root is None:
        return 0

    return 1 + count_nodes(root.left) + count_nodes(root.right)

def tree_sum(root):
    if root is None:
        return 0

    left_sum = tree_sum(root.left)
    right_sum = tree_sum(root.right)

    return root.val + left_sum + right_sum

def max_depth(root):
    if root is None:
        return 0

    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    if left_depth >= right_depth:
        return 1 + left_depth
    else:
        return 1 + right_depth


root = TreeNode(10, TreeNode(5), TreeNode(15))
print(max_depth(root))  # Expected: 2

root = TreeNode(
    10,
    TreeNode(5, TreeNode(2), TreeNode(7, TreeNode(3))),
    TreeNode(15)
)
print(max_depth(root))  # Expected: 4

print(max_depth(TreeNode(7)))  # Expected: 1
print(max_depth(None))         # Expected: 0