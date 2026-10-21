
def find_target_pair(nums, target):
    groups = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in groups:
            return [groups[complement], index]
        groups[num] = index



print(find_target_pair([2, 7, 11, 15], 9))
# Expected: [0, 1]

print(find_target_pair([3, 2, 4], 6))
# Expected: [1, 2]

print(find_target_pair([3, 3], 6))
# Expected: [0, 1]

print(find_target_pair([-3, 4, 3, 90], 0))
# Expected: [0, 2]

print(find_target_pair([1, 5, 8, 12], 13))
# Expected: [0, 3]
