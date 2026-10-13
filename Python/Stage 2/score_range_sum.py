# You are given an integer array scores, where scores[i] represents the points earned or lost during round i.
# You are also given two integers, start and end.
# Return the total points earned from round start through round end, inclusive.
# Your function must build a prefix sum array internally and use it to calculate the requested sum.

def score_range_sum(scores, start, end):
    prefix = []
    running_sum = 0

    for i in range(len(scores)):
        running_sum += scores[i]
        prefix.append(running_sum)

    if start == 0:
        return prefix[end]
    return prefix[end] - prefix[start-1]

print(score_range_sum([10, -5, 20, 15, -10], 1, 3))  # Expected: 30
print(score_range_sum([4, 8, -3, 6], 0, 2))         # Expected: 9
print(score_range_sum([1, 2, 3, 4, 5], 0, 4))       # Expected: 15
print(score_range_sum([7, -2, 9], 2, 2))            # Expected: 9
print(score_range_sum([-5, -3, -2, -1], 1, 3))      # Expected: -6
print(score_range_sum([20], 0, 0))                   # Expected: 20
print(score_range_sum([3, 6, 9, 12], 1, 2))         # Expected: 15