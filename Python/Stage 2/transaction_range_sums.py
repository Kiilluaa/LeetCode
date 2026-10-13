# You are given an integer array transactions, where each element represents a financial transaction.
# Positive numbers represent deposits, and negative numbers represent withdrawals.
# You are also given a list of queries, where each query contains two indices [start, end].
# For each query, calculate the sum of all transactions from index start through index end, inclusive.
# Return a list containing the results in the same order as the queries.
# Build the prefix sum array once and use it to answer every query.

def transaction_range_sums(transactions, queries):
    prefix = []
    running_sum = 0
    queried = []

    for i in transactions:
        running_sum += i
        prefix.append(running_sum)

    for left, right in queries:
        if left == 0:
            queried.append(prefix[right])
        else:
            queried.append(prefix[right] - prefix[left - 1])

    return queried

print(transaction_range_sums([100, -40, 20, -10, 50], [[0, 2], [1, 3], [2, 4]]))  # Expected: [80, -30, 60]
print(transaction_range_sums([5, -2, 7, -3], [[0, 3], [1, 2]]))                   # Expected: [7, 5]
print(transaction_range_sums([-10, -20, -30], [[0, 1], [1, 2], [2, 2]]))          # Expected: [-30, -50, -30]
print(transaction_range_sums([15], [[0, 0]]))                                      # Expected: [15]
print(transaction_range_sums([2, 4, 6, 8], [[0, 0], [0, 3], [2, 3]]))              # Expected: [2, 20, 14]
print(transaction_range_sums([3, 1, 5], [[1, 1], [0, 2], [1, 2]]))                 # Expected: [1, 9, 6]