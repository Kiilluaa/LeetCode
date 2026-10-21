# Given an array revenue, where each integer represents the revenue earned on one day, 
# and an integer days, return the maximum total revenue earned during exactly days consecutive days.
# Revenue values can be negative.


def best_revenue_period(revenue, days):
    left = 0
    run_sum = sum(revenue[:days])
    largest = run_sum

    for i in range(days, len(revenue)):
        run_sum += revenue[i]
        run_sum -= revenue[left]
        left += 1
        largest = max(largest, run_sum)
    return largest


print(best_revenue_period([4, 2, 7, 1, 5], 3))
# Expected: 13

print(best_revenue_period([3, 8, 2, 6], 2))
# Expected: 11

print(best_revenue_period([-4, -2, -7, -1], 2))
# Expected: -6

print(best_revenue_period([10, 20, 30], 3))
# Expected: 60

print(best_revenue_period([5, -2, 8, -1, 4], 2))
# Expected: 7
