# Given an array of integers nums and an integer k, 
# return the largest sum of any contiguous subarray containing exactly k elements.

def maximum_sum(nums, k):
    left = 0
    current_sum = 0

    for num in nums[:k]:
        current_sum += num

    largest_sum = current_sum

    for num in nums[k:]:
        current_sum += num
        current_sum -= nums[left]
        left += 1

        if current_sum > largest_sum:
            largest_sum = current_sum
        
    return largest_sum

print(maximum_sum([2, 1, 5, 1, 3, 2], 3))
# nums = [2, 1, 5, 1, 3, 2]
# k = 3