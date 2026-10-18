# A company stores its employee reporting structure as a binary tree. The CEO is at the root, 
# and each employee can have up to two direct reports.
# The company wants to determine the longest chain of employees from the CEO down to someone with no direct reports.
# Write longest_reporting_chain(root) to return the number of employees in the longest chain.


class Employee:
    def __init__(self, name, left=None, right=None):
        self.name = name
        self.left = left
        self.right = right


def longest_reporting_chain(root):
    def dfs(node):
        if node is None:
            return 0

        check_left = dfs(node.left)
        check_right = dfs(node.right)

        return 1 + max(check_left, check_right)

    return dfs(root)
        


# Test 1: Uneven organization
org1 = Employee("CEO")
org1.left = Employee("A")
org1.right = Employee("B")
org1.left.left = Employee("C")
org1.left.left.left = Employee("E")
org1.right.right = Employee("D")
print(longest_reporting_chain(org1))  # Expected: 4


# Test 2: Only CEO
print(longest_reporting_chain(Employee("CEO")))  # Expected: 1


# Test 3: Empty organization
print(longest_reporting_chain(None))  # Expected: 0


# Test 4: Two equal reporting chains
org4 = Employee("CEO")
org4.left = Employee("A", Employee("C"))
org4.right = Employee("B", None, Employee("D"))
print(longest_reporting_chain(org4))  # Expected: 3


# Test 5: One long reporting chain
org5 = Employee("CEO")
org5.right = Employee("A")
org5.right.left = Employee("B")
org5.right.left.right = Employee("C")
org5.right.left.right.left = Employee("D")
print(longest_reporting_chain(org5))  # Expected: 5
