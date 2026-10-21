# Write a function maximum_fixed_window(nums, k) that returns the largest sum of exactly k consecutive elements.
# Assume 1 <= k <= len(nums). Numbers may be negative.
# Complexity goals: O(n) time and O(1) auxiliary space.

def maximum_fixed_window(nums, k):
    left = 0
    run_sum = sum(nums[:k])
    largest = run_sum

    for i in range(k, len(nums)):
        run_sum -= nums[left]
        run_sum += nums[i]
        left += 1
        largest = max(largest, run_sum)
    return largest



print(maximum_fixed_window([2, 4, 1, 7, 3], 3))  # Expected: 12
print(maximum_fixed_window([1, 2, 3, 4], 2))     # Expected: 7
print(maximum_fixed_window([5, 1, 9, 2], 1))     # Expected: 9
print(maximum_fixed_window([-5, -2, -8], 2))     # Expected: -7
print(maximum_fixed_window([3, 1, 4], 3))        # Expected: 8
