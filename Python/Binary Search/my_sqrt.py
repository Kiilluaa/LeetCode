# Given a non-negative integer x, return the integer part of its square root.
# You cannot use Python's built-in square root functions or exponentiation.

def my_sqrt(x):
    left = 0
    right = x

    while left <= right:
        mid = (left + right) // 2

        if mid * mid == x:
            return mid
        elif mid * mid > x:
            right = mid - 1
        else:
            left = mid + 1
    return right

print(my_sqrt(0))          # Expected: 0
print(my_sqrt(1))          # Expected: 1
print(my_sqrt(2))          # Expected: 1
print(my_sqrt(4))          # Expected: 2
print(my_sqrt(8))          # Expected: 2
print(my_sqrt(9))          # Expected: 3
print(my_sqrt(15))         # Expected: 3
print(my_sqrt(16))         # Expected: 4
print(my_sqrt(20))         # Expected: 4
print(my_sqrt(25))         # Expected: 5
print(my_sqrt(99))         # Expected: 9
print(my_sqrt(100))        # Expected: 10
print(my_sqrt(101))        # Expected: 10
print(my_sqrt(10000))      # Expected: 100
print(my_sqrt(2147395599)) # Expected: 46339
print(my_sqrt(2147483647)) # Expected: 46340