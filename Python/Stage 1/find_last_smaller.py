def find_last_smaller(nums, target):
    smallest_index = -1
    for index, num in enumerate(nums):
        if num < target:
            smallest_index = index
    return smallest_index

print(find_last_smaller([8, 3, 7, 2, 9], 5))