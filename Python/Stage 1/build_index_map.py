# Goal: create a dictionary where each number maps to its index.

def build_index_map(nums):
    where = {}
    for index, num in enumerate(nums):
        where[num] = index
    return where

print(build_index_map([8, 3, 7]))