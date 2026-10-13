#  Given sorted ascending integers nums and target, return True if the target appears, otherwise
# False. A target may occur more than once.

def contains_sorted(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return True
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False



print(contains_sorted([1, 2, 2, 4, 9], 2)) # Expected: True
print(contains_sorted([1, 2, 2, 4, 9], 3)) # Expected: False
print(contains_sorted([], 3)) # Expected: False
print(contains_sorted([-4, -4, 0], -4)) # Expected: True