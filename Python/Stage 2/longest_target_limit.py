# Given an integer array nums, an integer target, 
# and an integer k, return the length of the longest contiguous 
# subarray containing at most k occurrences of target.
# Other integers may appear any number of times.

def longest_target_limit(nums, target, k):
    longest = 0
    counts = {}
    left = 0

    for right in range(len(nums)):
        counts[nums[right]] = counts.get(nums[right], 0) + 1

        while counts.get(target, 0) > k:
            counts[nums[left]] -= 1
            left += 1

        longest = max(longest, right - left + 1)
    return longest

print(longest_target_limit([1, 2, 1, 3, 1], 1, 2))    # Expected: 4
print(longest_target_limit([2, 5, 5, 3, 5, 4], 5, 1)) # Expected: 3
print(longest_target_limit([1, 2, 3, 4], 5, 0))       # Expected: 4
print(longest_target_limit([5, 5, 5], 5, 0))          # Expected: 0
print(longest_target_limit([5, 5, 5], 5, 3))          # Expected: 3
print(longest_target_limit([1, 2, 1, 2, 1], 1, 1))    # Expected: 3
print(longest_target_limit([], 3, 2))                  # Expected: 0
print(longest_target_limit([7, 7, 2, 3, 7], 7, 2))    # Expected: 4