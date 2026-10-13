# Given a binary array nums (containing only 0 and 1) and an integer k, return
#  the maximum number of consecutive 1s you can obtain by changing at most k zeros into ones.
# You do not need to modify the array. Return only the maximum possible length.

def longest_ones(nums, k):
    counts = {}
    left = 0
    longest = 0

    for right in range(len(nums)):
        counts[nums[right]] = counts.get(nums[right], 0) + 1

        while counts.get(0, 0) > k:
            counts[nums[left]] -= 1
        
            left += 1
        longest = max(longest, right - left + 1)
    return longest

print(longest_ones([1, 1, 0, 0, 1, 1, 1], 1))  # Expected: 4
print(longest_ones([0, 0, 1, 1, 0, 1, 1], 2))  # Expected: 6
print(longest_ones([1, 1, 1, 1], 0))           # Expected: 4
print(longest_ones([0, 0, 0], 0))              # Expected: 0
print(longest_ones([0, 0, 0], 3))              # Expected: 3
print(longest_ones([1, 0, 1, 0, 1], 1))        # Expected: 3
print(longest_ones([], 2))                     # Expected: 0
print(longest_ones([1, 0, 0, 1, 1, 0, 1], 2))  # Expected: 5