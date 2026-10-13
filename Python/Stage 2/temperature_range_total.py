# Problem: Historical Temperature Analysis
# You are given an integer array temperatures, where temperatures[i] represents the recorded temperature on day i.
# You are also given two integers, start and end.
# Return the sum of all recorded temperatures from day start through day end, inclusive.
# Your solution must use prefix sums rather than repeatedly adding the values in the requested range.

def temperature_range_total(temperatures, start, end):
    prefix = []
    running_sum = 0

    for i in range(len(temperatures)):
        running_sum += temperatures[i]
        prefix.append(running_sum)

    if start == 0:
        return prefix[end]
    return prefix[end] - prefix[start - 1]

print(temperature_range_total([12, -3, 8, 5, -2], 1, 3))  # Expected: 10
print(temperature_range_total([4, 7, -2, 9], 0, 2))       # Expected: 9
print(temperature_range_total([1, 2, 3, 4], 0, 3))        # Expected: 10
print(temperature_range_total([-5, -2, -7], 1, 2))        # Expected: -9
print(temperature_range_total([8], 0, 0))                 # Expected: 8
print(temperature_range_total([3, 6, 9, 12], 2, 3))       # Expected: 21
print(temperature_range_total([5, -5, 10, -10], 1, 3))   # Expected: -5