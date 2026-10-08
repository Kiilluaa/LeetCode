# You are given a list of integers nums sorted in ascending order and a non-negative integer target.
# Determine whether two different elements have an absolute difference equal to target.
# Return
# Return True if such a pair exists. Otherwise return False.

def pair_with_difference(nums, target):
    left = 0
    right = 1

    while right < len(nums):
        difference = nums[right] - nums[left]
        if difference < target:
            right += 1
        elif difference > target:
            left += 1

            if left == right:
                right += 1
        else:
            return True
    return False

print(pair_with_difference([1, 3, 5, 8, 12], 7))
print(pair_with_difference([2, 4, 7, 11], 6))