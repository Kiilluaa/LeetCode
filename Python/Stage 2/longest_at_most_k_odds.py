# Given an integer array nums and an integer k, return the length of 
# the longest contiguous subarray that contains at most k odd numbers.
# A subarray is a continuous sequence of elements within an array.
# An odd number is an integer that is not divisible by 2.

def longest_at_most_k_odds(nums, k):
    left = 0
    count = 0
    longest = 0

    for right in range(len(nums)):
        if nums[right] % 2 == 1:
            count += 1

        while count > k:
            if nums[left] % 2 == 1:
                count -= 1

            left += 1

        longest = max(longest, right - left + 1)

    return longest

print(longest_at_most_k_odds([2, 1, 4, 3, 6, 8], 1))  # Expected: 4
print(longest_at_most_k_odds([1, 3, 5, 2, 4], 2))     # Expected: 4
print(longest_at_most_k_odds([2, 4, 6, 8], 0))        # Expected: 4
print(longest_at_most_k_odds([1, 3, 5], 0))           # Expected: 0
print(longest_at_most_k_odds([1, 2, 3, 4, 5], 1))     # Expected: 3
print(longest_at_most_k_odds([], 2))                  # Expected: 0
print(longest_at_most_k_odds([1, 1, 2, 2, 1], 2))     # Expected: 4