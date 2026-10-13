nums = [2, 5, 8, 12, 16, 23, 38, 45, 56]
target = 23

def binary_search(nums, target):
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
    return -1

print(binary_search([2, 5, 8, 12, 16, 23, 38, 45, 56], 23)) # 5
print(binary_search([1, 3, 5, 7], 1)) # 0
print(binary_search([1, 3, 5, 7], 7)) # 3
print(binary_search([1, 3, 5, 7], 4)) # -1
print(binary_search([], 9)) # -1
print(binary_search([6], 6)) # 0
print(binary_search([6], 2)) # -1
