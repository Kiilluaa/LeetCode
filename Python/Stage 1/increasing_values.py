# Return a new list containing every number that is greater than the number immediately before it

def increasing_values(nums):
    new_list = []
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            new_list.append(nums[i])
    return new_list

print(increasing_values([3, 5, 2, 7, 7, 9]))