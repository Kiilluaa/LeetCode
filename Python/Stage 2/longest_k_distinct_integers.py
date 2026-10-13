# Given an integer array nums and an integer k, return the length of the longest contiguous 
# subarray containing at most k distinct integers.
# A distinct integer is a different numerical value, regardless of how many times it appears.

def longest_k_distinct_integers(nums, k):
    longest = 0
    left = 0
    counts = {}

    for right in range(len(nums)):
        counts[nums[right]] = counts.get(nums[right], 0) + 1

        while len(counts) > k:
            counts[nums[left]] -= 1

            if counts[nums[left]] == 0:
                del(counts[nums[left]])

            left += 1
        longest = max(longest, right - left + 1)
    return longest

print(longest_k_distinct_integers([1, 2, 1, 2, 3], 2))  # Expected: 4
print(longest_k_distinct_integers([1, 2, 3, 2, 2], 2))  # Expected: 4
print(longest_k_distinct_integers([5, 5, 5], 1))        # Expected: 3
print(longest_k_distinct_integers([1, 2, 3], 1))        # Expected: 1
print(longest_k_distinct_integers([1, 2, 1], 0))        # Expected: 0
print(longest_k_distinct_integers([], 2))               # Expected: 0
print(longest_k_distinct_integers([-1, -2, -1, 3], 2))  # Expected: 3