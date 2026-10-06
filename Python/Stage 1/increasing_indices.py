# Return the indexes of every number that is greater than the number immediately before it.

def increasing_indices(nums):
    indexes = []
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            indexes.append(i)
    return indexes

print(increasing_indices([3, 5, 2, 7, 7, 9]))