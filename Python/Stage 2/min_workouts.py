# You are given an integer array calories, where calories[i] represents the number of calories burned during workout i.
# You are also given a positive integer goal.
# Return the minimum number of consecutive workouts needed to burn at least goal calories.
# If no consecutive sequence reaches the goal, return 0.

def min_workouts(calories, goal):
    shortest = float("inf")
    left = 0
    total = 0

    for i in range(len(calories)):
        total += calories[i]

        while total >= goal:
            shortest = min(shortest, i - left + 1)
            total -= calories[left]
            left += 1

    if shortest == float("inf"):
        return 0
    return shortest

print(min_workouts([100, 200, 300, 150], 450))  # Expected: 2
print(min_workouts([50, 100, 75], 300))         # Expected: 0
print(min_workouts([500, 100, 200], 500))       # Expected: 1
print(min_workouts([100, 100, 100, 100], 300))  # Expected: 3
print(min_workouts([100, 250, 200, 150], 500))  # Expected: 3
print(min_workouts([], 300))                    # Expected: 0
print(min_workouts([200, 300], 500))            # Expected: 2
print(min_workouts([50, 50, 600, 50], 600))     # Expected: 1