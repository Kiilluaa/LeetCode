# You are given an integer array temperatures, where temperatures[i] represents the temperature recorded on day i.
# You are also given an integer k.
# Return the maximum sum of temperatures across exactly k consecutive days.
# Temperatures can be negative.

def max_temperature_sum(temperatures, k):
    largest = float("-inf")
    total = 0
    left = 0

    for i in range(len(temperatures)):
        total += temperatures[i]

        while i - left + 1 > k:
            total -= temperatures[left]
            left += 1

        if i - left + 1 == k:
            largest = max(largest, total)
    return largest

print(max_temperature_sum([3, -2, 5, 7, -1, 4], 3))  # Expected: 11
print(max_temperature_sum([-4, -2, -7, -3], 2))     # Expected: -6
print(max_temperature_sum([1, 2, 3, 4, 5], 2))      # Expected: 9
print(max_temperature_sum([10], 1))                  # Expected: 10
print(max_temperature_sum([5, 5, 5, 5], 3))         # Expected: 15
print(max_temperature_sum([8, -3, 2, -1], 2))       # Expected: 5
print(max_temperature_sum([-10, -20, -5], 1))       # Expected: -5
print(max_temperature_sum([2, -1, 3], 3))           # Expected: 4