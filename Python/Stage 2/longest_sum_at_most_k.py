# Given an array of non-negative integers nums and an integer k, return 
# the length of the longest contiguous subarray whose sum is less than or equal to k.
# A subarray consists of consecutive elements from the original array.

def longest_sum_at_most_k(nums, k):
    longest_sum_length = 0
    left = 0
    current_sum = 0

    for right in range(len(nums)):
        current_sum += nums[right]

        while current_sum > k:
            current_sum -= nums[left]
            left += 1
        longest_sum_length = max(right - left + 1, longest_sum_length)
    return longest_sum_length

print(longest_sum_at_most_k([2, 1, 3, 1, 1], 5))  # Expected: 3
print(longest_sum_at_most_k([4, 2, 1, 1, 3], 4))  # Expected: 3
print(longest_sum_at_most_k([1, 1, 1, 1], 2))     # Expected: 2
print(longest_sum_at_most_k([5, 6, 7], 3))        # Expected: 0
print(longest_sum_at_most_k([0, 0, 0], 0))        # Expected: 3
print(longest_sum_at_most_k([], 5))               # Expected: 0
print(longest_sum_at_most_k([1, 2, 3], 6))        # Expected: 3