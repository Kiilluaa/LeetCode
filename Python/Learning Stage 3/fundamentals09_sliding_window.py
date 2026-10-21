# Given a list of nonnegative integers, return the length of the longest contiguous subarray whose sum is at most k.


def longest_valid_window(nums, k):
    left = 0
    current_sum = 0
    longest = 0

    for right in range(len(nums)):
        current_sum += nums[right]

        while current_sum > k:
            current_sum -= nums[left]
            left += 1

        longest = max(longest, right - left + 1)

    return longest


print(longest_valid_window([2, 1, 3, 2, 1], 5))  # Expected: 2
print(longest_valid_window([1, 1, 1, 1], 3))     # Expected: 3
print(longest_valid_window([4, 2, 1, 1], 4))     # Expected: 3
print(longest_valid_window([5, 6, 7], 3))        # Expected: 0
print(longest_valid_window([], 5))               # Expected: 0
print(longest_valid_window([0, 0, 0], 0))        # Expected: 3
