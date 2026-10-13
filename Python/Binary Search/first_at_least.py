# Return the index of the first number greater than or equal to target.
# If no such number exists, return -1.

def first_at_least(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1
    if left == len(nums):
        return - 1
    return left

print(first_at_least([1, 3, 3, 5, 7, 9], 3))  # Expected: 1
print(first_at_least([2, 4, 6, 8], 5))        # Expected: 2
print(first_at_least([2, 4, 6, 8], 2))        # Expected: 0
print(first_at_least([2, 4, 6, 8], 10))       # Expected: -1
print(first_at_least([3, 3, 3, 3], 3))        # Expected: 0
print(first_at_least([3, 3, 3, 3], 4))        # Expected: -1
print(first_at_least([], 5))                  # Expected: -1
print(first_at_least([7], 7))                 # Expected: 0
print(first_at_least([7], 2))                 # Expected: 0