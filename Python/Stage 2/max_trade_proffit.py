# You are given an integer array profits, where profits[i] represents the profit or loss from trade i.
# You are also given an integer k.
# Return the maximum combined profit from exactly k consecutive trades.
# Positive values represent profits, and negative values represent losses.

def max_trade_profit(profits, k):
    maximum = float("-inf")
    left = 0
    total = 0

    for i in range(len(profits)):
        total += profits[i]

        while i - left + 1 >= k:
            maximum = max(maximum, total)
            total -= profits[left]
            left += 1
        
    return maximum

print(max_trade_profit([3, -2, 6, 4, -1], 3))  # Expected: 9
print(max_trade_profit([-8, -3, -5, -2], 2))  # Expected: -7
print(max_trade_profit([1, 2, 3, 4], 2))      # Expected: 7
print(max_trade_profit([10], 1))              # Expected: 10
print(max_trade_profit([5, 5, 5, 5], 3))     # Expected: 15
print(max_trade_profit([8, -3, 2, -1], 2))   # Expected: 5
print(max_trade_profit([-10, -20, -5], 1))   # Expected: -5
print(max_trade_profit([2, -1, 3], 3))       # Expected: 4