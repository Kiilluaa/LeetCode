# You are given an integer array production, where production[i] represents the number of units produced during hour i.
# You are also given an integer target.
# Return the minimum number of consecutive hours needed to produce at least target units.
# If no consecutive sequence reaches the target, return 0.

def min_production_hours(production, target):
    shortest = float("inf")
    left = 0
    total = 0

    for i in range(len(production)):
        total += production[i]

        while total >= target:
            shortest = min(shortest, i - left + 1)
            total -= production[left]
            left += 1
    if shortest == float("inf"):
        return 0
    return shortest

print(min_production_hours([1, 3, 2, 5, 1], 7))  # Expected: 2
print(min_production_hours([2, 2, 2], 7))        # Expected: 0
print(min_production_hours([9, 1, 2], 9))        # Expected: 1
print(min_production_hours([1, 2, 3, 4], 6))     # Expected: 2
print(min_production_hours([1, 1, 1, 1], 3))     # Expected: 3
print(min_production_hours([], 5))               # Expected: 0
print(min_production_hours([5], 5))              # Expected: 1