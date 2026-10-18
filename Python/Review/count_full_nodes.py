# Write a function count_full_nodes(root) that returns the number of nodes in a 
# binary tree that have both a left child and a right child.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_full_nodes(root):
    count = []

    def dfs(node):
        if node is None:
            return None
        
        if node.left and node.right:
            count.append(node.val)

        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return len(count)




# Test 1
tree1 = TreeNode(10)
tree1.left = TreeNode(5)
tree1.right = TreeNode(15)
tree1.left.left = TreeNode(3)
tree1.left.right = TreeNode(7)
tree1.right.right = TreeNode(20)
print(count_full_nodes(tree1))  # Expected: 2

# Test 2: Single node
print(count_full_nodes(TreeNode(8)))  # Expected: 0

# Test 3: Empty tree
print(count_full_nodes(None))  # Expected: 0

# Test 4: Every internal node has two children
tree4 = TreeNode(1)
tree4.left = TreeNode(2, TreeNode(4), TreeNode(5))
tree4.right = TreeNode(3, TreeNode(6), TreeNode(7))
print(count_full_nodes(tree4))  # Expected: 3

# Test 5: One-sided tree
tree5 = TreeNode(1)
tree5.right = TreeNode(2)
tree5.right.left = TreeNode(3)
print(count_full_nodes(tree5))  # Expected: 0
