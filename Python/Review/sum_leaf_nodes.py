# Given the root of a binary tree, return the sum of the values of all leaf nodes.
# A leaf node is a node with no left child and no right child.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sum_leaf_values(root):
    result = []

    def dfs(node):
        if node is None:
            return None
        elif not node.left and not node.right:
            result.append(node.val)

        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return sum(result)







# Test 1: Multiple leaf nodes
tree1 = TreeNode(10)
tree1.left = TreeNode(5)
tree1.right = TreeNode(15)
tree1.left.left = TreeNode(3)
tree1.left.right = TreeNode(7)
tree1.right.right = TreeNode(20)

print(sum_leaf_values(tree1))  # Expected: 30


# Test 2: Single node
tree2 = TreeNode(8)

print(sum_leaf_values(tree2))  # Expected: 8


# Test 3: Empty tree
print(sum_leaf_values(None))   # Expected: 0


# Test 4: Negative values
tree4 = TreeNode(5)
tree4.left = TreeNode(-3)
tree4.right = TreeNode(2)
tree4.right.left = TreeNode(-4)

print(sum_leaf_values(tree4))  # Expected: -7


# Test 5: Unbalanced tree
tree5 = TreeNode(1)
tree5.right = TreeNode(2)
tree5.right.right = TreeNode(3)
tree5.right.right.left = TreeNode(4)

print(sum_leaf_values(tree5))  # Expected: 4
