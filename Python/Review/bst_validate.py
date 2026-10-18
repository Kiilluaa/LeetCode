# Given the root of a binary tree, determine whether it is a valid Binary Search Tree (BST).
# A valid BST must satisfy these rules:
# - Every value in a node's left subtree must be strictly smaller than that node's value.
# - Every value in a node's right subtree must be strictly larger than that node's value.
# - These rules apply to the entire subtree, not just immediate children.
# - Duplicate values are not allowed.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def validate_search_tree(root):
    def dfs(node, up, low):
        if node is None:
            return True

        if low >= node.val or node.val >= up:
            return False

        check_left = dfs(node.left, node.val, low)
        check_right = dfs(node.right, up, node.val)

        return check_left and check_right
    return dfs(root, float("inf"), float("-inf"))

# Test 1: Valid BST
tree1 = TreeNode(10)
tree1.left = TreeNode(5)
tree1.right = TreeNode(15)
tree1.right.left = TreeNode(12)
tree1.right.right = TreeNode(20)

print(validate_search_tree(tree1))  # Expected: True


# Test 2: Invalid deeper node
tree2 = TreeNode(10)
tree2.left = TreeNode(5)
tree2.right = TreeNode(15)
tree2.right.left = TreeNode(6)
tree2.right.right = TreeNode(20)

print(validate_search_tree(tree2))  # Expected: False


# Test 3: Single node
print(validate_search_tree(TreeNode(8)))  # Expected: True


# Test 4: Empty tree
print(validate_search_tree(None))  # Expected: True


# Test 5: Duplicate value
tree5 = TreeNode(10)
tree5.left = TreeNode(5)
tree5.right = TreeNode(10)

print(validate_search_tree(tree5))  # Expected: False


# Test 6: Invalid node deep in left subtree
tree6 = TreeNode(20)
tree6.left = TreeNode(10)
tree6.right = TreeNode(30)
tree6.left.right = TreeNode(25)

print(validate_search_tree(tree6))  # Expected: False


# Test 7: Valid negative values
tree7 = TreeNode(0)
tree7.left = TreeNode(-10)
tree7.right = TreeNode(10)
tree7.left.right = TreeNode(-5)

print(validate_search_tree(tree7))  # Expected: True
