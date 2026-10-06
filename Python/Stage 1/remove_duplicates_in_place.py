# Assume nums is sorted.
# Your goal is to modify the same list so the unique values are moved to the front.

def remove_duplicates_in_place(nums):
    if not nums:
        return []
    
    count = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[count] = nums[i]
            count += 1
    return nums[:count]

print(remove_duplicates_in_place(nums = [1, 1, 2, 2, 3]))
print(remove_duplicates_in_place(nums = []))