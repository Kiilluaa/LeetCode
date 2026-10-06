# Given an integer array nums and an integer val, remove all occurrences of val in-place.
# The relative order of the remaining elements does not matter for this practice version.
# Return:
# Return the number of elements that are not equal to val.
# After the function finishes, the first k positions of nums should contain the remaining values, 
# where k is the returned number.

def remove_element(nums, val):
    read = 0
    write = 0

    while read < len(nums):
        if nums[read] == val:
            read += 1
        else:
            nums[write] = nums[read]
            read += 1
            write += 1

    return nums[:write], write



print(remove_element([3,2,2,3], 3))

# Input:
# nums = [3, 2, 2, 3]
# val = 3
# return 2 and nums[:2] == [2, 2]