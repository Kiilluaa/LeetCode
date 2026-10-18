# Write a function recursive_total(n) that returns the sum of all integers from 1 through n, inclusive.
# For example, if n = 5:
# 1 + 2 + 3 + 4 + 5 = 15
# Expected return: An integer.

def recursive_total(n):
    if n == 0:
        return 0

    return n + recursive_total(n - 1)    


print(recursive_total(5))    # Expected: 15
print(recursive_total(3))    # Expected: 6
print(recursive_total(1))    # Expected: 1
print(recursive_total(0))    # Expected: 0
print(recursive_total(10))   # Expected: 55
print(recursive_total(100))  # Expected: 5050
