# Given a list of non-negative integers nums and an integer k, 
# return the length of the longest contiguous subarray whose sum is less than or equal to k.

def longest_subarray(nums, k):

    current_longest = 0
    left = 0
    current_sum = 0

    for right in range(len(nums)):
        current_sum += nums[right]
        while current_sum > k:
            current_sum -= nums[left]
            left += 1

        current_longest = max(current_longest, right - left + 1)
        
    return current_longest

print(longest_subarray([2, 1, 3, 2, 1, 1], 5))