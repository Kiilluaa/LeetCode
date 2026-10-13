# You are given a list of integers nums sorted in ascending order and an integer target.
# Return the index of the last number that is less than or equal to target.
# If no such number exists, return -1.

def last_at_most(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    
    return right

print(last_at_most([1, 3, 3, 5, 7, 9], 3))  # Expected: 2
print(last_at_most([2, 4, 6, 8], 5))        # Expected: 1
print(last_at_most([2, 4, 6, 8], 2))        # Expected: 0
print(last_at_most([2, 4, 6, 8], 1))        # Expected: -1
print(last_at_most([2, 4, 6, 8], 10))       # Expected: 3
print(last_at_most([3, 3, 3, 3], 3))        # Expected: 3
print(last_at_most([3, 3, 3, 3], 2))        # Expected: -1
print(last_at_most([], 5))                 # Expected: -1
print(last_at_most([7], 7))                # Expected: 0
print(last_at_most([7], 10))               # Expected: 0