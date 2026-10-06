def find_first_negative(nums):
    for index, num in enumerate(nums):
        if num < 0:
            return index
    return -1

print(find_first_negative([5, 8, -2, 7, -9]))