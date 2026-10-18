# Write a function recursive_square_sum(n) that returns the sum of the squares of all integers from 1 through n.

def recursive_square_sum(n):
    if n == 0:
        return 0

    return n*n + recursive_square_sum(n - 1)


print(recursive_square_sum(4))   # Expected: 30
print(recursive_square_sum(3))   # Expected: 14
print(recursive_square_sum(1))   # Expected: 1
print(recursive_square_sum(0))   # Expected: 0
print(recursive_square_sum(5))   # Expected: 55
print(recursive_square_sum(10))  # Expected: 385
