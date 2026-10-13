# You are given an array of positive integers transactions, where transactions[i] represents the amount spent in transaction i.
# You are also given a positive integer threshold.
# Return the minimum number of consecutive transactions whose combined spending is greater than or equal to threshold.
# If no consecutive sequence reaches the threshold, return 0.

def min_transactions(transactions, threshold):
    shortest = float("inf")
    left = 0
    total = 0

    for i in range(len(transactions)):
        total += transactions[i]

        while total >= threshold:
            shortest = min(shortest, i - left + 1)
            total -= transactions[left]
            left += 1

    if shortest == float("inf"):
        return 0
    return shortest

print(min_transactions([3, 2, 6, 1, 4], 8))  # Expected: 2
print(min_transactions([1, 2, 3], 10))       # Expected: 0
print(min_transactions([10, 1, 2], 10))      # Expected: 1
print(min_transactions([2, 2, 2, 2], 6))     # Expected: 3
print(min_transactions([1, 4, 2, 3], 7))     # Expected: 3
print(min_transactions([], 5))               # Expected: 0
print(min_transactions([5, 5], 10))          # Expected: 2
print(min_transactions([1, 1, 9, 1], 9))     # Expected: 1