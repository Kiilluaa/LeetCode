# A company organizes its employees into a hierarchy represented by a binary tree.
# Each employee has a performance score represented by an integer. The company has established a 
# minimum score that employees must exceed to qualify for a bonus.
# Your task is to determine how many employees throughout the organization qualify for the bonus.
# The CEO is included in the evaluation, and every employee must be considered, regardless of their position in the hierarchy.


class Employee:
    def __init__(self, score=0, left=None, right=None):
        self.score = score
        self.left = left
        self.right = right


def count_bonus_eligible(root, minimum_score):

    def dfs(node, min):
        if node is None:
            return 0

        check_left = dfs(node.left, min)
        check_right = dfs(node.right, min)

        if node.score > min:
            return 1 + check_left + check_right
        else:
            return check_left + check_right

    return dfs(root, minimum_score)


# Test 1: Mixed performance scores
org1 = Employee(85)
org1.left = Employee(70)
org1.right = Employee(95)
org1.left.left = Employee(90)
org1.left.right = Employee(60)
org1.right.left = Employee(80)
org1.right.right = Employee(100)

print(count_bonus_eligible(org1, 80))  # Expected: 4


# Test 2: Nobody qualifies
print(count_bonus_eligible(org1, 100))  # Expected: 0


# Test 3: Everyone qualifies
print(count_bonus_eligible(org1, 50))  # Expected: 7


# Test 4: Empty organization
print(count_bonus_eligible(None, 75))  # Expected: 0


# Test 5: Single employee
print(count_bonus_eligible(Employee(90), 80))  # Expected: 1


# Test 6: Scores equal to threshold
org6 = Employee(75)
org6.left = Employee(75)
org6.right = Employee(80)

print(count_bonus_eligible(org6, 75))  # Expected: 1


# Test 7: Negative scores
org7 = Employee(-5)
org7.left = Employee(-10)
org7.right = Employee(0)

print(count_bonus_eligible(org7, -6))  # Expected: 2
