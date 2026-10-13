# Given an integer array nums, return a new array where 
# each element is the sum of all elements up to and including that index.

def build_prefix(nums):
    prefix = []
    running_sum = 0

    for i in range(len(nums)):
        running_sum += nums[i]
        prefix.append(running_sum)

    return prefix

print(build_prefix([2, 4, 3, 5]))