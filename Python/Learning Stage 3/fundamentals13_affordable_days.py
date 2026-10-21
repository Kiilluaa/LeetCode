# A traveler records how much money they spend each day. Given a list of 
# daily expenses and a budget, find the maximum number of consecutive days they can travel 
# without the total expenses exceeding their budget.


def longest_affordable_stretch(expenses, budget):
    left = 0
    longest = 0
    run_sum = 0

    for i in range(len(expenses)):
        run_sum += expenses[i]

        while run_sum > budget:
            run_sum -= expenses[left]
            left += 1

        longest = max(longest, i - left + 1)
    return longest


print(longest_affordable_stretch([2, 1, 3, 1, 2], 5))
# Expected: 3

print(longest_affordable_stretch([1, 1, 1, 1], 2))
# Expected: 2

print(longest_affordable_stretch([5, 6, 7], 3))
# Expected: 0

print(longest_affordable_stretch([4, 2, 1, 1], 4))
# Expected: 3

print(longest_affordable_stretch([], 10))
# Expected: 0

print(longest_affordable_stretch([0, 0, 0], 0))
# Expected: 3
