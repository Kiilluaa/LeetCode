def count_target(nums, target):
    count = 0
    for num in nums:
        if num == target:
            count += 1
    return count

print(count_target([1, 4, 2, 4, 4], 4))