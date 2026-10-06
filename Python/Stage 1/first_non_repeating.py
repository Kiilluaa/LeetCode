# Return the first value that appears exactly once in the entire list.
# If every value repeats, return -1.

def first_non_repeating(nums):
    frequency = {}

    for num in nums:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    for num in nums:
        if frequency[num] == 1:
            return num
    return -1


print(first_non_repeating([4, 5, 1, 2, 1, 4, 5]))