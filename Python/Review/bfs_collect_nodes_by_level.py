# Given the root of a binary tree, return a list containing all node values in level-order traversal, from left to right.


from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def collect_nodes_by_level(root):
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
tree1 = TreeNode(8)
tree1.left = TreeNode(4)
tree1.right = TreeNode(12)
tree1.left.left = TreeNode(2)
tree1.left.left.left = TreeNode(1)
tree1.right.left = TreeNode(10)
tree1.right.right = TreeNode(14)

print(collect_nodes_by_level(tree1))
# Expected: [8, 4, 12, 2, 10, 14, 1]


# Test 2: Single node
print(collect_nodes_by_level(TreeNode(5)))
# Expected: [5]


# Test 3: Empty tree
print(collect_nodes_by_level(None))
# Expected: []


# Test 4: Balanced tree
tree4 = TreeNode(20)
tree4.left = TreeNode(10, TreeNode(5), TreeNode(15))
tree4.right = TreeNode(30, TreeNode(25), TreeNode(35))

print(collect_nodes_by_level(tree4))
# Expected: [20, 10, 30, 5, 15, 25, 35]


# Test 5: Right-skewed tree
tree5 = TreeNode(1)
tree5.right = TreeNode(2)
tree5.right.right = TreeNode(3)
tree5.right.right.right = TreeNode(4)

print(collect_nodes_by_level(tree5))
# Expected: [1, 2, 3, 4]


# Test 6: Missing children
tree6 = TreeNode(9)
tree6.left = TreeNode(4)
tree6.right = TreeNode(15)
tree6.left.right = TreeNode(6)
tree6.right.left = TreeNode(12)

print(collect_nodes_by_level(tree6))
# Expected: [9, 4, 15, 6, 12]
