# return how many times a number is greater than the number immediately before it

def count_increases(nums):
    count = 0
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            count += 1
    return count

print(count_increases([3, 5, 2, 7, 7, 9]))