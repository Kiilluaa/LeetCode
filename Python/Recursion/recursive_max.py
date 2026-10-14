def recursive_max(nums, index=0):
    if index == len(nums):
        return float("-inf")

    remaining_max = recursive_max(nums, index + 1)
    if nums[index] > remaining_max:
        return nums[index]
    
    return remaining_max


print(recursive_max([3, 9, 2, 7]))       # Expected: 9
print(recursive_max([5]))                # Expected: 5
print(recursive_max([-8, -2, -10]))      # Expected: -2
print(recursive_max([10, 10, 3]))        # Expected: 10
print(recursive_max([1, 2, 3, 4, 5]))    # Expected: 5
print(recursive_max([9, 7, 5, 3, 1]))    # Expected: 9