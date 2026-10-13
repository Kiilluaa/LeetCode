# You are given an integer array energy, where energy[i] represents the net energy consumed during hour i.
# Positive values represent consumption, while negative values represent energy returned to the system.
# You are also given two integers, start and end.
# Return the total net energy consumed from index start through index end, inclusive.
# Your function should preprocess the array using prefix sums and calculate the requested range efficiently.

def energy_range_total(energy, start, end):
    prefix = []
    running_sum = 0

    for i in energy:
        running_sum += i
        prefix.append(running_sum)

    if start == 0:
        return prefix[end]
    return prefix[end] - prefix[start - 1]

print(energy_range_total([5, -2, 8, 3, -4], 1, 3))  # Expected: 9
print(energy_range_total([4, 6, -3, 7], 0, 2))     # Expected: 7
print(energy_range_total([1, 2, 3, 4], 0, 3))      # Expected: 10
print(energy_range_total([-5, -2, -7], 1, 2))      # Expected: -9
print(energy_range_total([8], 0, 0))               # Expected: 8
print(energy_range_total([3, 6, 9, 12], 2, 3))     # Expected: 21
print(energy_range_total([5, -5, 10, -10], 1, 3)) # Expected: -5