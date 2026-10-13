def lower_bound(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1
    
    return left

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

def count_occurrences(nums, target):
    lower = lower_bound(nums, target)
    upper = upper_bound(nums, target)

    return upper - lower

print(count_occurrences([1, 2, 2, 2, 3, 4], 2))  # Expected: 3
print(count_occurrences([1, 3, 5, 7], 4))        # Expected: 0
print(count_occurrences([5, 5, 5, 5], 5))        # Expected: 4
print(count_occurrences([1, 2, 3, 4], 1))        # Expected: 1
print(count_occurrences([], 5))                 # Expected: 0
print(count_occurrences([2, 2, 4, 4, 4], 4))     # Expected: 3