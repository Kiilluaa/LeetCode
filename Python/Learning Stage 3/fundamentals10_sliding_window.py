# Given a list of nonnegative integers representing item costs and an integer budget,
#  find the maximum number of consecutive items whose combined cost does not exceed the budget.
# You cannot skip items between the beginning and end of a selected group.


def longest_affordable_group(costs, budget):
    left = 0
    running_sum = 0
    longest = 0

    for i in range(len(costs)):
        running_sum += costs[i]

        while running_sum > budget:
            running_sum -= costs[left]
            left += 1

        longest = max(longest, i - left +1)
    return longest


print(longest_affordable_group([3, 1, 2, 4, 1], 6))
# Expected: 3

print(longest_affordable_group([1, 1, 1, 1], 2))
# Expected: 2

print(longest_affordable_group([5, 6, 7], 3))
# Expected: 0

print(longest_affordable_group([2, 3, 1, 1, 2], 5))
# Expected: 3

print(longest_affordable_group([], 10))
# Expected: 0

print(longest_affordable_group([0, 0, 0, 2], 0))
# Expected: 3

print(longest_affordable_group([4, 2, 1, 1], 4))
# Expected: 3
