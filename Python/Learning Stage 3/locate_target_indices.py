# Given an array of integers numbers and an integer goal, find the indices of two different elements whose values add up to goal.
# You may assume exactly one valid pair exists. Return the indices in any order.


def locate_target_indices(numbers, goal):
    collection = {}
    for index, num in enumerate(numbers):
        comp = goal - num
        if comp in collection:
            return [collection[comp], index]
        collection[num] = index


print(locate_target_indices([4, 10, 6, 3], 9))
# Expected: [2, 3]

print(locate_target_indices([8, 1, 5, 2], 10))
# Expected: [0, 3]

print(locate_target_indices([5, 5], 10))
# Expected: [0, 1]

print(locate_target_indices([-4, 7, 2, 9], 3))
# Expected: [0, 1]

print(locate_target_indices([12, 3, 8, 15], 20))
# Expected: [0, 2]

print(locate_target_indices([1, 6, 11, 4], 15))
# Expected: [2, 3]
