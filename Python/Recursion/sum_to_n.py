def sum_to_n(n):
    if n < 1:
        return 0
    return n + (sum_to_n(n - 1))

print(sum_to_n(0))    # Expected: 0
print(sum_to_n(1))    # Expected: 1
print(sum_to_n(4))    # Expected: 10
print(sum_to_n(5))    # Expected: 15
print(sum_to_n(10))   # Expected: 55
print(sum_to_n(100))  # Expected: 5050