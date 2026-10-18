# Given the root of a Binary Search Tree containing unique product IDs and an integer product_id, 
# return True if the product exists or False if it doesn't.
# The tree follows standard BST ordering rules.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def product_exists(root, product_id):
    current = root
    if current is None:
        return False

    while current:
        if current.val == product_id:
            return True
        elif current.val > product_id:
            current = current.left
        else:
            current = current.right

    return False


# Test 1: Balanced BST
tree1 = TreeNode(50)
tree1.left = TreeNode(25)
tree1.right = TreeNode(75)
tree1.left.left = TreeNode(10)
tree1.left.right = TreeNode(30)
tree1.right.left = TreeNode(60)
tree1.right.right = TreeNode(90)

print(product_exists(tree1, 60))  # Expected: True
print(product_exists(tree1, 40))  # Expected: False
print(product_exists(tree1, 50))  # Expected: True
print(product_exists(tree1, 10))  # Expected: True


# Test 2: Empty tree
print(product_exists(None, 25))  # Expected: False


# Test 3: Single node
print(product_exists(TreeNode(8), 8))  # Expected: True
print(product_exists(TreeNode(8), 4))  # Expected: False


# Test 4: Right-skewed BST
tree4 = TreeNode(5)
tree4.right = TreeNode(10)
tree4.right.right = TreeNode(15)
tree4.right.right.right = TreeNode(20)

print(product_exists(tree4, 20))  # Expected: True
print(product_exists(tree4, 12))  # Expected: False


# Test 5: Negative IDs
tree5 = TreeNode(0)
tree5.left = TreeNode(-20)
tree5.right = TreeNode(20)
tree5.left.right = TreeNode(-10)

print(product_exists(tree5, -10))  # Expected: True
