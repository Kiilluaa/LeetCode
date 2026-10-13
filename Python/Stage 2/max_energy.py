# You are given an integer array energy, where energy[i] represents the net energy generated during hour i.
# You are also given an integer k.
# Return the maximum total energy generated during exactly k consecutive hours.
# Energy values may be negative, representing energy consumption exceeding production.

def max_energy(energy, k):
    longest = float("-inf")
    left = 0
    total = 0

    for i in range(len(energy)):
        total += energy[i]

        while i - left + 1 > k:
            total -= energy[left]
            left += 1

        if i - left + 1 == k:
            longest = max(longest, total)
    return longest

print(max_energy([4, -2, 5, 3, -1, 6], 3))  # Expected: 8
print(max_energy([-5, -3, -7, -2], 2))     # Expected: -8
print(max_energy([1, 2, 3, 4], 2))         # Expected: 7
print(max_energy([10], 1))                 # Expected: 10
print(max_energy([5, 5, 5, 5], 3))        # Expected: 15
print(max_energy([8, -3, 2, -1], 2))      # Expected: 5
print(max_energy([-10, -20, -5], 1))      # Expected: -5
print(max_energy([2, -1, 3], 3))          # Expected: 4