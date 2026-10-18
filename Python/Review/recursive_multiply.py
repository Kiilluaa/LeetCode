# Write a function recursive_multiply(n) that returns the product of all positive integers from 1 through n.


def recursive_multiply(n):
    if n == 0:
        return 1

    return n * recursive_multiply(n - 1)


print(recursive_multiply(4))  # Expected: 24
print(recursive_multiply(5))  # Expected: 120
print(recursive_multiply(3))  # Expected: 6
print(recursive_multiply(1))  # Expected: 1
print(recursive_multiply(0))  # Expected: 1
print(recursive_multiply(6))  # Expected: 720
