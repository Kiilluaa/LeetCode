# Given the root of a binary tree, return a list containing every node's value in preorder traversal.
# Preorder visits nodes in this order:
# Root → Left → Right


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder_values(root):
    preorder = []
    def dfs(node):
        if node is None:
            return None

        preorder.append(node.val)
        dfs(node.left)
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
print(preorder_values(tree1))
# Expected: [10, 5, 3, 7, 15, 20]


# Test 2: Single node
print(preorder_values(TreeNode(8)))
# Expected: [8]


# Test 3: Empty tree
print(preorder_values(None))
# Expected: []


# Test 4: Left-skewed tree
tree4 = TreeNode(1)
tree4.left = TreeNode(2)
tree4.left.left = TreeNode(3)
print(preorder_values(tree4))
# Expected: [1, 2, 3]


# Test 5: Mixed branches
tree5 = TreeNode(4)
tree5.left = TreeNode(2, TreeNode(1), TreeNode(3))
tree5.right = TreeNode(6, TreeNode(5), TreeNode(7))
print(preorder_values(tree5))
# Expected: [4, 2, 1, 3, 6, 5, 7]
