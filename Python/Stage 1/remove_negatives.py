# Modify nums in-place so that all non-negative values are moved to the front while keeping their original order.
# Return the number of non-negative values.
# You do not need to remove the leftover values at the end of the list. Only the first k positions matter, where k is the value you return.

def remove_negatives(nums):
    write = 0

    for read in range(len(nums)):
        if nums[read] >= 0:
            nums[write], nums[read] = nums[read], nums[write]
            write += 1
    return write

nums = [-2, 4, -1, 7, 0, -3]
print(remove_negatives(nums))   # Expected: 3
print(nums[:3])                 # Expected: [4, 7, 0]

# nums = [1, 2, 3]
# print(remove_negatives(nums))   # Expected: 3
# print(nums[:3])                 # Expected: [1, 2, 3]

# nums = [-5, -2, -1]
# print(remove_negatives(nums))   # Expected: 0
# print(nums[:0])                 # Expected: []