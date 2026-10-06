# You are given a sorted list of integers nums in non-decreasing order.
# Return a new list containing the square of each number, also sorted in non-decreasing order.

def sorted_squares(nums):
    result = [0] * len(nums)
    left = 0
    right = len(nums) - 1
    count = len(nums) - 1

    while left <= right:
        squareLeft = nums[left] * nums[left]
        squareRight = nums[right] * nums[right]
        if squareLeft > squareRight:
            result[count] = squareLeft
            left += 1
            count -= 1
        else:
            result[count] = squareRight
            right -= 1
            count -= 1

    return result

print(sorted_squares([-4, -1, 0, 3, 10]))
print(sorted_squares([-8, 0, 3, 9, 10]))

# Input: nums = [-4, -1, 0, 3, 10]
# Output: [0, 1, 9, 16, 100]