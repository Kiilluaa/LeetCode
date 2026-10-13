# Given an integer array sales and two integers left and right, return the 
# sum of all sales from index left through index right, inclusive.
# You must first build a prefix sum array and then use it to calculate the requested range sum.

def sales_range_sum(sales, left, right):
    prefix = []
    running_sum = 0

    for i in range(len(sales)):
        running_sum += sales[i]
        prefix.append(running_sum)

    if left == 0:
        return prefix[right]
    return prefix[right] - prefix[left - 1]

print(sales_range_sum([5, 10, 3, 7, 2], 1, 3))  # Expected: 20
print(sales_range_sum([4, 6, 2, 8], 0, 2))      # Expected: 12
print(sales_range_sum([1, 2, 3, 4], 0, 3))      # Expected: 10
print(sales_range_sum([7, 5, 9], 2, 2))         # Expected: 9
print(sales_range_sum([-3, 5, -2, 8], 1, 3))   # Expected: 11
print(sales_range_sum([10], 0, 0))              # Expected: 10