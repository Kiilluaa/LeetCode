# You are given an integer array pages, where pages[i] represents the number of pages in chapter i.
# You are also given a positive integer goal.
# Return the minimum number of consecutive chapters needed to read at least goal pages.
# If no consecutive sequence reaches the goal, return 0.

def min_chapters(pages, goal):
    total = 0
    left = 0
    shortest = float("inf")

    for i in range(len(pages)):
        total += pages[i]

        while total >= goal:
            total -= pages[left]
            shortest = min(shortest, i - left + 1)
            left += 1

    if shortest == float("inf"):
        return 0
    return shortest

print(min_chapters([10, 20, 15, 5, 25], 30))  # Expected: 2
print(min_chapters([5, 5, 5], 20))            # Expected: 0
print(min_chapters([30], 30))                 # Expected: 1
print(min_chapters([8, 12, 7, 10], 19))       # Expected: 2
print(min_chapters([1, 2, 3, 4], 6))          # Expected: 2
print(min_chapters([], 10))                   # Expected: 0
print(min_chapters([4, 4, 4, 4], 8))          # Expected: 2