# Given an ascending list of distinct integers nums and an integer target, return its index, or -1 if
# absent. This is the same pattern as LeetCode 704, but write it from memory.

def find_target(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

print(find_target([-9, -3, 0, 4, 11], 4)) # Expected: 3
print(find_target([-9, -3, 0, 4, 11], 2)) # Expected: -1
print(find_target([5], 5)) # Expected: 0
print(find_target([], 5)) # Expected: -1
