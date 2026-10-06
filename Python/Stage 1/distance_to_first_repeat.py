# Scan left to right.
# When you encounter the first value that has appeared before, return how far apart the two occurrences are.

def distance_to_first_repeat(nums):
    seen = {}
    for index, num in enumerate(nums):
        if num not in seen:
            seen[num] = index
        else:
            return index - seen[num]
    return -1

print(distance_to_first_repeat([5, 2, 7, 5, 2]))