def multiple_range_sums(nums, queries):
    prefix = []
    running_sum = 0
    queried = []

    for i in nums:
        running_sum += i
        prefix.append(running_sum)

    # prefix = [2, 6, 9, 14, 20]
    # queried = [9, 14 - 2, 20 - 6]
    for left, right in queries:
        if left == 0:
            queried.append(prefix[right])
        else:
            queried.append(prefix[right] - prefix[left - 1])


    return queried

print(multiple_range_sums([2,4,3,5,6], [[0,2], [1,3], [2,4]]))


# nums = [2, 4, 3, 5, 6]

# queries = [
#     [0, 2],
#     [1, 3],
#     [2, 4]
# ]