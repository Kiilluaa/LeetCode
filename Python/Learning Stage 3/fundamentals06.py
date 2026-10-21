numbers = [1, 3, 4, 6, 8, 11]
target = 10


def has_target_pair(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return True
        elif total > target:
            right -= 1
        else:
            left += 1
    return False


print(has_target_pair([1, 3, 4, 6, 8, 11], 10))  # True
print(has_target_pair([1, 2, 3, 4], 10))          # False
print(has_target_pair([2, 5], 7))                 # True
print(has_target_pair([3], 6))                    # False
print(has_target_pair([], 10))                    # False
print(has_target_pair([-5, -2, 0, 3, 9], 1))     # True
