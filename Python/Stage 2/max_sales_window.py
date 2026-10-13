# Given an array of integers sales, where sales[i] represents the sales made 
# on day i, and an integer k, return the maximum total sales across exactly k consecutive days.
# The array may contain negative values, representing losses.
# You may assume 1 <= k <= len(sales).

def max_sales_window(sales, k):
    maximum = float("-inf")
    total = 0
    left = 0

    for i in range(len(sales)):
        total += sales[i]

        while i - left + 1 > k:
            total -= sales[left]
            left += 1

        if i - left + 1 == k:
            maximum = max(maximum, total)
            
    return maximum

print(max_sales_window([2, 5, 1, 8, 3, 4], 3))  # Expected: 14
print(max_sales_window([-5, -2, -8, -1], 2))   # Expected: -7
print(max_sales_window([1, 2, 3, 4], 2))       # Expected: 7
print(max_sales_window([10], 1))               # Expected: 10
print(max_sales_window([4, 4, 4, 4], 3))       # Expected: 12
print(max_sales_window([3, -2, 5, -1], 2))     # Expected: 3
print(max_sales_window([1, 2, 3], 3))          # Expected: 6