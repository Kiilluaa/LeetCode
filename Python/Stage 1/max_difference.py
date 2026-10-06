# Return the largest difference between a later number and an earlier number.

def max_difference(nums):
    smallest = None
    largest_difference = 0
    for num in nums:
        if smallest is None or num < smallest:
            smallest = num
        if num - smallest > largest_difference:
            largest_difference = num - smallest
    return largest_difference

print(max_difference([7, 1, 5, 3, 6, 4]))