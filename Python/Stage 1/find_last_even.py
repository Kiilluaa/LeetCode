def find_last_even(nums):
    last = -1
    for index, num in enumerate(nums):
        if num % 2 == 0:
            last = index
    return last

print(find_last_even([5, 8, 3, 10, 7]))