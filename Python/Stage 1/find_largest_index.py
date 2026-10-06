def find_largest_index(nums):
    largest = None
    biggest = -1
    for index, num in enumerate(nums):
        if largest is None or num > largest:
            largest = num
            biggest = index
    return biggest

print(find_largest_index([4, 9, 2, 7]))