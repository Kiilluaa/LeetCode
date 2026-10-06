def find_first_greater(nums, target):
    for index, num in enumerate(nums):
        if num > target:
            return index
    return -1

print(find_first_greater([2, 4, 7, 3], 5))