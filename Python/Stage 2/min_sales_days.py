# You are given an integer array sales, where sales[i] represents the number of products sold on day i.
# You are also given a positive integer goal.
# Return the minimum number of consecutive days needed to sell at least goal products.
# If there is no sequence of consecutive days that reaches the goal, return 0.

def min_sales_days(sales, goal):
    shortest = float("inf")
    left = 0
    total = 0

    for i in range(len(sales)):
        total += sales[i]

        while total >= goal:
            shortest = min(shortest, i - left + 1)
            total -= sales[left]
            left += 1
    if shortest == float("inf"):
        return 0
    
    return shortest

print(min_sales_days([1, 2, 3, 4, 2], 7))  # Expected: 2
print(min_sales_days([2, 2, 2], 5))        # Expected: 3
print(min_sales_days([1, 1, 1], 6))        # Expected: 0
print(min_sales_days([8, 1, 1], 8))        # Expected: 1
print(min_sales_days([1, 2, 1, 2, 1], 4))  # Expected: 3
print(min_sales_days([], 10))              # Expected: 0
print(min_sales_days([3, 1, 2, 1, 1], 6))  # Expected: 3