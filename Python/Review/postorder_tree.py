# Given the root of a binary tree, return a list containing every node's value in postorder traversal.
# Postorder visits nodes in this order:
# Left → Right → Root


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def postorder_values(root):
    preorder = []
    def dfs(node):
        if node is None:
            return None

        dfs(node.left)
        dfs(node.right)
        preorder.append(node.val)
    dfs(root)
    return preorder


# Test 1: Multiple branches
tree1 = TreeNode(10)
tree1.left = TreeNode(5)
tree1.right = TreeNode(15)
tree1.left.left = TreeNode(3)
tree1.left.right = TreeNode(7)
tree1.right.right = TreeNode(20)

print(postorder_values(tree1))
# Expected: [3, 7, 5, 20, 15, 10]


# Test 2: Single node
print(postorder_values(TreeNode(8)))
# Expected: [8]


# Test 3: Empty tree
print(postorder_values(None))
# Expected: []


# Test 4: Left-skewed tree
tree4 = TreeNode(5)
tree4.left = TreeNode(3)
tree4.left.left = TreeNode(1)

print(postorder_values(tree4))
# Expected: [1, 3, 5]


# Test 5: Mixed branches
tree5 = TreeNode(8)
tree5.left = TreeNode(4, TreeNode(2), TreeNode(6))
tree5.right = TreeNode(12, TreeNode(10), TreeNode(14))

print(postorder_values(tree5))
# Expected: [2, 6, 4, 10, 14, 12, 8]


# Test 6: Right-skewed tree
tree6 = TreeNode(1)
tree6.right = TreeNode(2)
tree6.right.right = TreeNode(3)
tree6.right.right.right = TreeNode(4)

print(postorder_values(tree6))
# Expected: [4, 3, 2, 1]
