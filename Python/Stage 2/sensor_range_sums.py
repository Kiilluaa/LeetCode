# You are given an integer array readings, where readings[i] represents a sensor's recorded value at time i.
# You are also given a list of queries. Each query contains two indices [left, right].
# For every query, calculate the sum of the sensor readings from index left through index right, inclusive.
# Return a list containing the sums in the same order as the queries.
# You must build the prefix sum array once and use it to answer all queries.

def sensor_range_sums(readings, queries):
    prefix = []
    running_sum = 0
    quereied = []

    for i in readings:
        running_sum += i
        prefix.append(running_sum)

    for left, right in queries:
        if left == 0:
            quereied.append(prefix[right])
        else:
            quereied.append(prefix[right] - prefix[left - 1])

    return quereied

print(sensor_range_sums([4, -2, 7, 3, -1], [[0, 2], [1, 3], [2, 4]]))  # Expected: [9, 8, 9]
print(sensor_range_sums([10, 5, -3, 8], [[0, 3], [2, 2]]))           # Expected: [20, -3]
print(sensor_range_sums([1, 2, 3, 4], [[0, 0], [0, 3], [1, 2]]))      # Expected: [1, 10, 5]
print(sensor_range_sums([-5, -2, -7], [[0, 1], [1, 2]]))             # Expected: [-7, -9]
print(sensor_range_sums([8], [[0, 0]]))                               # Expected: [8]
print(sensor_range_sums([3, 6, 9, 12], [[1, 3], [2, 2], [0, 2]]))    # Expected: [27, 9, 18]