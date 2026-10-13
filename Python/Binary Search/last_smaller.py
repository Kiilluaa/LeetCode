# You are given a list of integers nums, sorted in ascending order, and an integer target.
# Return the index of the last number strictly smaller than target.
# If no number is smaller than the target, return -1.

def last_smaller(nums, target):
    left = 0
    right = len(nums) -1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1
    return right

print(last_smaller([1, 3, 3, 5, 7, 9], 5))  # Expected: 2
print(last_smaller([2, 4, 6, 8], 2))        # Expected: -1
print(last_smaller([2, 4, 6, 8], 7))        # Expected: 2
print(last_smaller([1, 2, 2, 2, 5], 2))     # Expected: 0
print(last_smaller([5, 5, 5], 5))           # Expected: -1
print(last_smaller([1, 3, 5, 7], 10))       # Expected: 3
print(last_smaller([], 3))                 # Expected: -1
print(last_smaller([10], 5))               # Expected: -1
print(last_smaller([10], 15))              # Expected: 0