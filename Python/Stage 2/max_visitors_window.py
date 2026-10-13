# You are given an integer array visitors, where visitors[i] represents the number of visitors during hour i.
# You are also given an integer k.
# Return the maximum total number of visitors across exactly k consecutive hours.
# Visitor counts can be negative.

def max_visitors_window(visitors, k):
    max_visitors = float("-inf")
    left = 0
    total = 0

    for i in range(len(visitors)):
        total += visitors[i]

        while i - left + 1 > k:
            total -= visitors[left]
            left += 1

        if i - left + 1 == k:
            max_visitors = max(max_visitors, total)
    return max_visitors

print(max_visitors_window([4, 1, 7, -2, 6, 3], 3))  # Expected: 11
print(max_visitors_window([-3, -6, -1, -8], 2))     # Expected: -7
print(max_visitors_window([1, 2, 3, 4], 2))         # Expected: 7
print(max_visitors_window([9], 1))                  # Expected: 9
print(max_visitors_window([2, 2, 2, 2], 3))        # Expected: 6
print(max_visitors_window([5, -1, 4, -2], 2))      # Expected: 4
print(max_visitors_window([-5, -4, -3], 1))        # Expected: -3
print(max_visitors_window([3, 1, 2], 3))           # Expected: 6