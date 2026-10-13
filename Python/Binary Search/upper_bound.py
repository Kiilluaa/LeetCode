def upper_bound(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return left

print(upper_bound([1, 3, 3, 3, 5, 7], 3))  # Expected: 4
print(upper_bound([2, 4, 6, 8], 5))        # Expected: 2
print(upper_bound([2, 4, 6, 8], 10))       # Expected: 4
print(upper_bound([2, 4, 6, 8], 1))        # Expected: 0
print(upper_bound([], 5))                 # Expected: 0