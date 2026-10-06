# Return the indexes of two different numbers where the later number minus the earlier number equals target.
# Assume exactly one valid answer exists.
# Return the indexes as a list: [earlier_index, later_index].

def two_difference(nums, target):
    diff_index = {}

    for index, num in enumerate(nums):
        complement = num - target

        if complement in diff_index:
            return [diff_index[complement], index]

        diff_index[num] = index

print(two_difference([1, 4, 7, 10], 6))