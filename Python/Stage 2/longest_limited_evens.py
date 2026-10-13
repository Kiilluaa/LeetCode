# Given an integer array nums and an integer k, return the length of the longest contiguous subarray containing at most k even numbers.
# A subarray is a continuous sequence of elements in the original array.

def longest_limited_evens(nums, k):
    longest = 0
    left = 0
    count = 0

    for right in range(len(nums)):
        if nums[right] % 2 == 0:
            count += 1

        while count > k:
            if nums[left] % 2 == 0:
                count -= 1
            left += 1
        longest = max(longest, right - left + 1)
    
    return longest

print(longest_limited_evens([1, 2, 3, 4, 5, 7], 1))  # Expected: 4
print(longest_limited_evens([2, 4, 6, 1, 3], 2))     # Expected: 4
print(longest_limited_evens([1, 3, 5, 7], 0))        # Expected: 4
print(longest_limited_evens([2, 4, 6], 0))           # Expected: 0
print(longest_limited_evens([1, 2, 3, 4, 5], 1))     # Expected: 3
print(longest_limited_evens([], 2))                  # Expected: 0
print(longest_limited_evens([2, 1, 2, 1, 2], 2))     # Expected: 4