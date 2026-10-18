# Given the root of a binary tree, return a list of all node values in 
# level-order traversal, visiting each level from left to right.


from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bfs_tree_values(root):
    if root is None:
        return None

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


# Test 1: Uneven tree
tree1 = TreeNode(20)
tree1.left = TreeNode(10)
tree1.right = TreeNode(30)
tree1.left.left = TreeNode(5)
tree1.left.right = TreeNode(15)
tree1.right.right = TreeNode(40)
tree1.left.right.left = TreeNode(12)

print(bfs_tree_values(tree1))
# Expected: [20, 10, 30, 5, 15, 40, 12]


# Test 2: Single node
print(bfs_tree_values(TreeNode(100)))
# Expected: [100]


# Test 3: Empty tree
print(bfs_tree_values(None))
# Expected: []


# Test 4: Balanced tree
tree4 = TreeNode(50)
tree4.left = TreeNode(25, TreeNode(10), TreeNode(35))
tree4.right = TreeNode(75, TreeNode(60), TreeNode(90))

print(bfs_tree_values(tree4))
# Expected: [50, 25, 75, 10, 35, 60, 90]


# Test 5: Left-skewed tree
tree5 = TreeNode(9)
tree5.left = TreeNode(7)
tree5.left.left = TreeNode(5)
tree5.left.left.left = TreeNode(3)

print(bfs_tree_values(tree5))
# Expected: [9, 7, 5, 3]


# Test 6: Missing children
tree6 = TreeNode(1)
tree6.left = TreeNode(2)
tree6.right = TreeNode(3)
tree6.left.right = TreeNode(4)
tree6.right.left = TreeNode(5)
tree6.right.left.right = TreeNode(6)

print(bfs_tree_values(tree6))
# Expected: [1, 2, 3, 4, 5, 6]
