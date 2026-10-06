# Given an integer array nums, move all odd values to the front of the same list while preserving their original order.
# Return:
# Return the number of odd values.
# After the function finishes, the first k positions of nums should contain the odd values, where k is the returned number.

def keep_odds(nums):
    read = 0
    write = 0
    while read < len(nums):
        if nums[read] % 2 == 0:
            read += 1
        else:
            nums[write] = nums[read]
            read += 1
            write += 1
    return write

print(keep_odds([2, 7, 4, 9, 6, 3]))

# Input:
# nums = [2, 7, 4, 9, 6, 3]
# nums[:3] == [7, 9, 3]
# Return:
# 3