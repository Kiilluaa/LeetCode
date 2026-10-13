# Given an integer array nums, repeatedly remove pairs of adjacent identical numbers until no more adjacent pairs can be removed.
# Return the remaining numbers as a list, preserving their original order.
# Removing a pair may cause previously separated numbers to become adjacent, creating another pair that must be removed.

def remove_adjacent_numbers(nums):
    stack = []

    for i in nums:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    return stack

print(remove_adjacent_numbers([1, 2, 2, 1, 3]))   # Expected: [3]
print(remove_adjacent_numbers([4, 5, 5, 6, 6, 4])) # Expected: []
print(remove_adjacent_numbers([1, 1, 1, 1]))      # Expected: []
print(remove_adjacent_numbers([1, 2, 3]))         # Expected: [1, 2, 3]
print(remove_adjacent_numbers([7, 7, 8]))         # Expected: [8]
print(remove_adjacent_numbers([3, 3, 3]))         # Expected: [3]
print(remove_adjacent_numbers([]))                # Expected: []
print(remove_adjacent_numbers([-1, -1, 2, 2]))    # Expected: []
print(remove_adjacent_numbers([1, 2, 2, 3, 3, 1])) # Expected: []