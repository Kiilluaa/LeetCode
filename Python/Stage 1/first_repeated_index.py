# Scan left to right.
# Return the index where you first encounter a value that has already appeared before.
# If no value repeats, return -1.

def first_repeated_index(nums):
    first = {}

    for index, num in enumerate(nums):
        if num in first:
            return index
        else:
            first[num] = index
    return -1

print(first_repeated_index([5, 2, 7, 5, 2]))