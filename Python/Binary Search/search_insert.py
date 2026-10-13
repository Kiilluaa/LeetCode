def search_insert(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

print(search_insert([1, 3, 5, 6], 5)) # Expected: 2
print(search_insert([1, 3, 5, 6], 2)) # Expected: 1
print(search_insert([1, 3, 5, 6], 7)) # Expected: 4
print(search_insert([1, 3, 5, 6], 0)) # Expected: 0
print(search_insert([], 3)) # Expected: 0
print(search_insert([10], 9)) # Expected: 0
print(search_insert([10], 12)) # Expected: 1
