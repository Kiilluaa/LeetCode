# A company represents its management hierarchy as a binary tree. Each node represents an employee, 
# and each employee can directly supervise up to two other employees.
# The HR department considers a manager overloaded when they have at least one direct 
# report and the total number of employees reporting to them, directly or indirectly, is greater than a given limit.
# Given the root of the organization and an integer limit, return how many managers are overloaded.



class Employee:
    def __init__(self, name, left=None, right=None):
        self.name = name
        self.left = left
        self.right = right


def count_overloaded_managers(root, limit):
    def dfs(node):
        if node is None:
            return 0, 0

        left_size, left_overloaded = dfs(node.left)
        right_size, right_overloaded = dfs(node.right)

        reports = left_size + right_size
        subtree_size = 1 + reports

        overloaded_count = left_overloaded + right_overloaded

        if reports > limit:
            overloaded_count += 1

        return subtree_size, overloaded_count

    total_size, total_overloaded = dfs(root)
    return total_overloaded


# Test 1
org1 = Employee("CEO")
org1.left = Employee("A")
org1.right = Employee("B")
org1.left.left = Employee("C")
org1.left.right = Employee("D")
org1.left.left.left = Employee("F")
org1.right.right = Employee("E")
print(count_overloaded_managers(org1, 2))  # Expected: 2


# Test 2: Nobody overloaded
print(count_overloaded_managers(org1, 10))  # Expected: 0


# Test 3: Every manager overloaded
print(count_overloaded_managers(org1, 0))  # Expected: 4


# Test 4: Empty organization
print(count_overloaded_managers(None, 1))  # Expected: 0


# Test 5: Single employee
print(count_overloaded_managers(Employee("CEO"), 0))  # Expected: 0


# Test 6: Small hierarchy
org6 = Employee("CEO")
org6.left = Employee("A")
org6.right = Employee("B")
print(count_overloaded_managers(org6, 1))  # Expected: 1
