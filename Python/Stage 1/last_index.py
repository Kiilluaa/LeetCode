# Build a dictionary where each number maps to the last index where it appears.
# Later duplicates should overwrite earlier indexes.

def last_index_map(nums):
    last_index = {}
    for index, num in enumerate(nums):
        last_index[num] = index
    return last_index

print(last_index_map([5, 2, 5, 7, 2]))