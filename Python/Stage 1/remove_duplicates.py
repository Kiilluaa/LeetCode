# Assume nums is sorted.
# Return a new list containing each value only once.

def remove_duplicates(nums):

    if not nums:
        return []

    new_nums = [nums[0]]

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            new_nums.append(nums[i])
    return new_nums

print(remove_duplicates([1, 1, 2, 2, 2, 3, 5, 5]))
print(remove_duplicates([]))