# Modify nums in place so that all non-zero values stay
# in their original relative order, and all zeros move to the end.
#
# Return: nums

def move_zeros(nums):
    if not nums:
        return []

    write = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[write] = nums[i]
            write += 1
    for i in range(write, len(nums)):
        nums[i] = 0
        write += 1
    return nums

print(move_zeros(nums = [0, 1, 0, 3, 12]))