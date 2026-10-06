# Return how many times a number is smaller than the number immediately before it

def count_decreases(nums):
    count = 0
    for i in range(1, len(nums)):
        if nums[i] < nums[i-1]:
            count += 1
    return count