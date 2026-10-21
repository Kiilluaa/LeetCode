numbers = [4, 9, 12, 3, 15, 8]

# Write code that finds the index of the first number greater than 10.
# Your program should print the index, not the number. If no number qualifies, print -1.

saved = -1
for index, num in enumerate(numbers):
    if num > 10:
        saved = index
        break
print(saved)