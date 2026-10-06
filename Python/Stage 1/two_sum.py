# Return the indexes of two different numbers that add up to target.
# Assume exactly one valid answer exists.
# Return the indexes as a list.

def two_sum(nums, target):
    seen = {}
    for index, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], index]

        seen[num] = index


print(two_sum([2, 7, 11, 15], 9))