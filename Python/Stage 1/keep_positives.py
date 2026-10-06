# Given an integer array nums, move all positive values to the front of the same list while preserving their original order.
# Return:
# Return the number of positive values.
# After the function finishes, the first k positions of nums should contain the positive values, 
# where k is the returned number.

def keep_positives(nums):
    read = 0
    write = 0
    while read < len(nums):
        if nums[read] < 1:
            read += 1
        else:
            nums[write] = nums[read]
            read += 1
            write += 1
    return write

print(keep_positives([-2, 4, 0, 7, -1, 3]))
# Input:
# nums = [-2, 4, 0, 7, -1, 3]
# Return:
# nums[:3] == [4, 7, 3]