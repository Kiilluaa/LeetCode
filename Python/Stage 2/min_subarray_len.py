# Given an array of positive integers nums and a positive integer target, 
# return the minimum length of a contiguous subarray whose sum is greater than or equal to target.
# If no such subarray exists, return 0.

def min_subarray_len(target, nums):
    minimum_len = float("inf")
    left = 0
    current_sum = 0

    for right in range(len(nums)):
        current_sum += nums[right]

        while current_sum >= target:
            minimum_len = min(minimum_len, right - left + 1)
            current_sum -= nums[left]
            left += 1

    if minimum_len == float("inf"):
        return 0
    else:
        return minimum_len



print(min_subarray_len(3, [3, 1, 1, 1, 1, 1]))  # Expected: 1
print(min_subarray_len(7, [2, 3, 1, 2, 4, 3]))  # Expected: 2
print(min_subarray_len(4, [1, 4, 4]))           # Expected: 1
print(min_subarray_len(11, [1, 1, 1, 1]))       # Expected: 0
print(min_subarray_len(5, [5]))                 # Expected: 1
print(min_subarray_len(15, [1, 2, 3, 4, 5]))    # Expected: 5
print(min_subarray_len(6, [1, 2, 3, 4]))        # Expected: 2
print(min_subarray_len(7, []))                  # Expected: 0