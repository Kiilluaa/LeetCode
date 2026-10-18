# Given the root of a Binary Search Tree and an integer target, 
# return True if the target exists in the tree, or False otherwise.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# def bst_contains_value(root, target):
#     def dfs(node, target):
#         if node is None:
#             return

#         check_left = dfs(node.left, target)
#         check_right = dfs(node.right, target)

#         return check_right or check_left
#     return dfs(root, target)

def bst_contains_value(root, target):
    current = root

    while current:
        if current.val == target:
            return True
        elif current.val > target:
            current = current.left
        else:
            current = current.right
    return False


# Test 1: Balanced BST
tree1 = TreeNode(10)
tree1.left = TreeNode(5)
tree1.right = TreeNode(15)
tree1.left.left = TreeNode(3)
tree1.left.right = TreeNode(7)
tree1.right.left = TreeNode(12)
tree1.right.right = TreeNode(20)

print(bst_contains_value(tree1, 12))  # Expected: True
print(bst_contains_value(tree1, 8))   # Expected: False
print(bst_contains_value(tree1, 10))  # Expected: True
print(bst_contains_value(tree1, 3))   # Expected: True


# Test 2: Empty tree
print(bst_contains_value(None, 5))    # Expected: False


# Test 3: Single node
print(bst_contains_value(TreeNode(8), 8))  # Expected: True
print(bst_contains_value(TreeNode(8), 4))  # Expected: False


# Test 4: Right-skewed BST
tree4 = TreeNode(1)
tree4.right = TreeNode(3)
tree4.right.right = TreeNode(5)
tree4.right.right.right = TreeNode(7)

print(bst_contains_value(tree4, 7))   # Expected: True
print(bst_contains_value(tree4, 4))   # Expected: False


# Test 5: Negative values
tree5 = TreeNode(0)
tree5.left = TreeNode(-10)
tree5.right = TreeNode(10)
tree5.left.right = TreeNode(-5)

print(bst_contains_value(tree5, -5))  # Expected: True
