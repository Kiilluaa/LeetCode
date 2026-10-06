# Goal: store each number as the key and its square as the value.

def build_square_map(nums):
    squares = {}
    for num in nums:
        squares[num] = num * num
    return squares

print(build_square_map([2, 3, 4]))