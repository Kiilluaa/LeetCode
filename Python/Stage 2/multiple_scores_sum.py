# You are given an integer array scores and a list of queries.
# Each query is a pair [left, right], and for each query you must 
# return the sum of scores[left] through scores[right], inclusive.
# Build the prefix sum array once, then use it to answer all queries.

def multiple_score_sums(scores, queries):
    prefix = []
    running_sum = 0
    queried = []

    for i in scores:
        running_sum += i
        prefix.append(running_sum)

    for left, right in queries:
        if left == 0:
            queried.append(prefix[right])
        else:
            queried.append(prefix[right] - prefix[left - 1])

    return queried

print(multiple_score_sums([3, 5, 2, 7, 4], [[0, 2], [1, 3], [2, 4]]))   # Expected: [10, 14, 13]
print(multiple_score_sums([10, -2, 6, 1], [[0, 0], [0, 3], [1, 2]]))    # Expected: [10, 15, 4]
print(multiple_score_sums([5, 5, 5, 5], [[0, 1], [1, 3], [2, 2]]))      # Expected: [10, 15, 5]
print(multiple_score_sums([8], [[0, 0]]))                                # Expected: [8]
print(multiple_score_sums([-3, 4, -2, 7], [[0, 2], [1, 3], [3, 3]]))    # Expected: [-1, 9, 7]