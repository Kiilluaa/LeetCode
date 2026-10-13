# You are given an integer array expenses, where expenses[i] represents the net 
# expense recorded on day i. Values may be positive or negative.
# You are also given two integers, left and right.
# Return the sum of expenses from index left through index right, inclusive.
# Your function must build a prefix sum array internally and use it to calculate the range sum.

def expense_range_sum(expenses, left, right):
    prefix = []
    running_sum = 0

    for i in range(len(expenses)):
        running_sum += expenses[i]
        prefix.append(running_sum)

    if left == 0:
        return prefix[right]
    return prefix[right] - prefix[left - 1]

print(expense_range_sum([8, -3, 12, 5, -2], 1, 3))  # Expected: 14
print(expense_range_sum([6, 4, -2, 9], 0, 2))      # Expected: 8
print(expense_range_sum([1, 2, 3, 4, 5], 0, 4))    # Expected: 15
print(expense_range_sum([7, -2, 9], 2, 2))         # Expected: 9
print(expense_range_sum([-5, -3, -2, -1], 1, 3))   # Expected: -6
print(expense_range_sum([20], 0, 0))                # Expected: 20
print(expense_range_sum([3, 6, 9, 12], 1, 2))      # Expected: 15