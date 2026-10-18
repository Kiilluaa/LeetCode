# Given the root of a binary tree, return a list containing every node's value in inorder traversal.
# Inorder visits nodes in this order:
# Left → Root → Right


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_values(root):
    preorder = []
    def dfs(node):
        if node is None:
            return None

        dfs(node.left)
        preorder.append(node.val)
        dfs(node.right)
    dfs(root)
    return preorder


# Test 1: Multiple branches
tree1 = TreeNode(10)
tree1.left = TreeNode(5)
tree1.right = TreeNode(15)
tree1.left.left = TreeNode(3)
tree1.left.right = TreeNode(7)
tree1.right.right = TreeNode(20)

print(inorder_values(tree1))
# Expected: [3, 5, 7, 10, 15, 20]


# Test 2: Single node
print(inorder_values(TreeNode(8)))
# Expected: [8]


# Test 3: Empty tree
print(inorder_values(None))
# Expected: []


# Test 4: Left-skewed tree
tree4 = TreeNode(5)
tree4.left = TreeNode(3)
tree4.left.left = TreeNode(1)

print(inorder_values(tree4))
# Expected: [1, 3, 5]


# Test 5: Mixed branches
tree5 = TreeNode(8)
tree5.left = TreeNode(4, TreeNode(2), TreeNode(6))
tree5.right = TreeNode(12, TreeNode(10), TreeNode(14))

print(inorder_values(tree5))
# Expected: [2, 4, 6, 8, 10, 12, 14]


# Test 6: Not a binary search tree
tree6 = TreeNode(10)
tree6.left = TreeNode(20)
tree6.right = TreeNode(5)

print(inorder_values(tree6))
# Expected: [20, 10, 5]
