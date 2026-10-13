# You are given a list of integers nums sorted in ascending order and an integer target.
# Return the index of the first number strictly greater than target.
# If no number is greater than the target, return -1.

def first_greater(nums, target):
    left = 0
    right = len(nums) -1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1
    if left == len(nums):
        return -1
    return left

print(first_greater([1, 3, 3, 5, 7, 9], 3))  # Expected: 3
print(first_greater([2, 4, 6, 8], 10))       # Expected: -1
print(first_greater([2, 4, 6, 8], 1))        # Expected: 0
print(first_greater([1, 2, 2, 2, 5], 2))     # Expected: 4
print(first_greater([5, 5, 5], 5))           # Expected: -1
print(first_greater([1, 3, 5, 7], 4))        # Expected: 2
print(first_greater([], 3))                 # Expected: -1
print(first_greater([10], 5))               # Expected: 0