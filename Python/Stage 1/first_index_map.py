# Build a dictionary where each number maps to the first index where it appeared.
# If a number appears again later, do not overwrite its original index.

def first_index_map(nums):
    first_index = {}
    for index, num in enumerate(nums):
        if num not in first_index:
            first_index[num] = index
    return first_index


print(first_index_map([5, 2, 5, 7, 2]))