# Return True if there are two different numbers in the list whose sum equals target. Otherwise return False.

def has_pair_with_sum(nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            print(nums[left], nums[right])
            return True
        elif current_sum < target:
            left += 1
        elif current_sum > target:
            right -= 1
    return False

print(has_pair_with_sum([2, 7, 8, 11, 15], 9))