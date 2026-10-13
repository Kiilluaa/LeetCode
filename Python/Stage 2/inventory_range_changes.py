# You are given an integer array changes, where changes[i] represents the change in warehouse inventory on day i.
# Positive values represent incoming inventory, while negative values represent outgoing inventory.
# You are also given a list of queries, where each query contains two integers [start, end].
# For each query, return the total inventory change from index start through index end, inclusive.
# Return a list of results in the same order as the queries.

def inventory_range_changes(changes, queries):
    prefix = []
    running_sum = 0
    queried = []

    for i in changes:
        running_sum += i
        prefix.append(running_sum)

    for left, right in queries:
        if left == 0:
            queried.append(prefix[right])
        else:
            queried.append(prefix[right] - prefix[left - 1])

    return queried

print(inventory_range_changes([10, -4, 6, -2, 8], [[0, 2], [1, 3], [2, 4]]))  # Expected: [12, 0, 12]
print(inventory_range_changes([-5, 3, 7, -1], [[0, 3], [1, 2]]))             # Expected: [4, 10]
print(inventory_range_changes([2, 4, 6], [[0, 0], [0, 2], [1, 2]]))           # Expected: [2, 12, 10]
print(inventory_range_changes([-3, -2, -1], [[0, 1], [1, 2]]))               # Expected: [-5, -3]
print(inventory_range_changes([8], [[0, 0]]))                                 # Expected: [8]
print(inventory_range_changes([1, 2, 3], []))                                 # Expected: []
print(inventory_range_changes([5, -5, 10, -10], [[0, 3], [1, 3]]))           # Expected: [0, -5]