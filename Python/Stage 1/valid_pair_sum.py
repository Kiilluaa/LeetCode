# You are given a sorted list of integers nums and an integer target.
# Return True if there are two different elements whose sum equals target. Otherwise return False.

def valid_pair_sum(nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
        if nums[left] + nums[right] == target:
            return True
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            left += 1
    return False

print(valid_pair_sum([1, 2, 4, 6, 10], 8))
        

# Input: nums = [1, 2, 4, 6, 10], target = 8
# Output: True