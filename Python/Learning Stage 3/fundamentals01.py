numbers = [3, 8, 12, 5, 10, 7]

# Creates a variable named total.
# Loops through numbers.
# Adds a number to total only when that number is greater than 6.
# Prints the final total.

total = 0
for num in numbers:
    if num > 6:
        total += num
print(total)