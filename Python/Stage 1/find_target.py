def find_target(nums, target):
    for index, num in enumerate(nums):
        if num == target:
            return index

    return -1

print(find_target([8, 3, 7, 3], 3))