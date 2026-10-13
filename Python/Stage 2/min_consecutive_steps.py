# You are given an array steps, where steps[i] represents the positive distance traveled during step i.
# Given an integer distance, return the minimum number of consecutive steps whose combined distance is at least distance.
# Return 0 if no such sequence exists.

def min_consecutive_steps(steps, distance):
    left = 0
    shortest = float("inf")
    total = 0

    for i in range(len(steps)):
        total += steps[i]

        while total >= distance:
            shortest = min(shortest, i - left + 1)
            total -= steps[left]
            left += 1
    if shortest == float("inf"):
        return 0
    return shortest

print(min_consecutive_steps([2, 1, 5, 2, 3], 7))  # Expected: 2
print(min_consecutive_steps([1, 2, 1], 8))        # Expected: 0
print(min_consecutive_steps([10, 2, 3], 10))      # Expected: 1
print(min_consecutive_steps([1, 1, 1, 1], 3))     # Expected: 3
print(min_consecutive_steps([3, 2, 4, 1], 6))     # Expected: 2
print(min_consecutive_steps([], 5))               # Expected: 0
print(min_consecutive_steps([5, 5], 10))          # Expected: 2