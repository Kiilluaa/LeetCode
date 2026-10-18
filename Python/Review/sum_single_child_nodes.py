# Given the root of a binary tree, return the sum of the values of all nodes that have exactly one child.
# A node qualifies when:
# - It has a left child but no right child.
# - OR it has a right child but no left child.
# Nodes with zero or two children do not qualify.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sum_single_child_nodes(root):
    result = []

    def dfs(node):
        if node is None:
            return None

        dfs(node.left)
        dfs(node.right)

        if node.left and not node.right:
            result.append(node.val)
        elif node.right and not node.left:
            result.append(node.val)

    dfs(root)
    return sum(result)

# Test 1: Multiple qualifying nodes
tree1 = TreeNode(10)
tree1.left = TreeNode(5)
tree1.right = TreeNode(15)
tree1.left.left = TreeNode(3)
tree1.left.left.left = TreeNode(2)
tree1.right.right = TreeNode(20)
print(sum_single_child_nodes(tree1))  # Expected: 23


# Test 2: Single node
print(sum_single_child_nodes(TreeNode(8)))  # Expected: 0


# Test 3: Empty tree
print(sum_single_child_nodes(None))  # Expected: 0


# Test 4: No qualifying nodes
tree4 = TreeNode(10)
tree4.left = TreeNode(5)
tree4.right = TreeNode(15)
print(sum_single_child_nodes(tree4))  # Expected: 0


# Test 5: Negative values
tree5 = TreeNode(-10)
tree5.left = TreeNode(-5)
tree5.left.right = TreeNode(3)
print(sum_single_child_nodes(tree5))  # Expected: -15
