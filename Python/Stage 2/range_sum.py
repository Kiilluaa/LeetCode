def range_sum(prefix, left, right):
    if left == 0:
        return prefix[right]
    return prefix[right] - prefix[left -1]

prefix = [2, 9, 12, 17, 21, 27]

print(range_sum(prefix, 0, 3))  # Expected: 17
print(range_sum(prefix, 2, 4))  # Expected: 12
print(range_sum(prefix, 1, 5))  # Expected: 25
print(range_sum(prefix, 0, 0))  # Expected: 2
print(range_sum(prefix, 3, 3))  # Expected: 5