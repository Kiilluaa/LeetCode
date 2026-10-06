def count_positive(nums):
    count = 0
    for num in nums:
        if num > 0:
            count += 1
    return count

print(count_positive([3, -1, 0, 8, -4]))