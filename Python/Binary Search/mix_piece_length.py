# You are given an integer length representing the length of a rope and 
# an integer k representing how many equal-sized pieces you need.
# You can cut the rope into pieces of equal integer length. You may discard any leftover rope.
# Return the maximum integer length each piece can have while producing at least k pieces.
# If it's impossible to produce k pieces of positive integer length, return 0.

def max_piece_length(length, k):
    left = 0
    right = length

    while left <= right:
        mid = (left + right) // 2
        if mid * k == length:
            return mid
        elif mid * k > length:
            right = mid - 1
        else:
            left = mid + 1
    
    return right

print(max_piece_length(20, 3))     # Expected: 6
print(max_piece_length(15, 5))     # Expected: 3
print(max_piece_length(4, 6))      # Expected: 0
print(max_piece_length(10, 2))     # Expected: 5
print(max_piece_length(10, 3))     # Expected: 3
print(max_piece_length(25, 4))     # Expected: 6
print(max_piece_length(100, 10))   # Expected: 10
print(max_piece_length(7, 1))      # Expected: 7
print(max_piece_length(0, 5))      # Expected: 0
print(max_piece_length(1, 1))      # Expected: 1
print(max_piece_length(100, 101))  # Expected: 0
print(max_piece_length(1000000000, 3))  # Expected: 333333333