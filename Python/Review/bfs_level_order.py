# Given the root of a binary tree, return a list of its node values in level-order traversal.
# Visit nodes from top to bottom, processing each level from left to right.


from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order_values(root):
    if root is None:
        return []

    order = []
    queue = deque([root])

    while queue:
        current = queue.popleft()
        order.append(current.val)

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)

    return order


# Test 1: Multiple levels
tree1 = TreeNode(10)
tree1.left = TreeNode(5)
tree1.right = TreeNode(15)
tree1.left.left = TreeNode(3)
tree1.left.right = TreeNode(7)
tree1.right.right = TreeNode(20)

print(level_order_values(tree1))
# Expected: [10, 5, 15, 3, 7, 20]


# Test 2: Single node
print(level_order_values(TreeNode(8)))
# Expected: [8]


# Test 3: Empty tree
print(level_order_values(None))
# Expected: []


# Test 4: Balanced tree
tree4 = TreeNode(1)
tree4.left = TreeNode(2, TreeNode(4), TreeNode(5))
tree4.right = TreeNode(3, TreeNode(6), TreeNode(7))

print(level_order_values(tree4))
# Expected: [1, 2, 3, 4, 5, 6, 7]


# Test 5: One-sided tree
tree5 = TreeNode(1)
tree5.right = TreeNode(2)
tree5.right.right = TreeNode(3)
tree5.right.right.right = TreeNode(4)

print(level_order_values(tree5))
# Expected: [1, 2, 3, 4]


# Test 6: Uneven branches
tree6 = TreeNode(9)
tree6.left = TreeNode(4)
tree6.right = TreeNode(12)
tree6.left.right = TreeNode(6)
tree6.right.left = TreeNode(10)

print(level_order_values(tree6))
# Expected: [9, 4, 12, 6, 10]
