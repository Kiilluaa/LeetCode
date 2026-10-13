# Given a sorted ascending list nums (duplicates allowed) and a target, return the first index
# containing a value >= target. If none exists, return len(nums). This is often called a lower bound.

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


print(lower_bound([1, 2, 2, 2, 5], 2)) # Expected: 1
print(lower_bound([1, 2, 2, 2, 5], 3)) # Expected: 4
print(lower_bound([1, 2, 2, 2, 5], 9)) # Expected: 5
print(lower_bound([], 3)) # Expected: 0