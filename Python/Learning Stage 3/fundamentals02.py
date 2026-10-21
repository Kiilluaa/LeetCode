numbers = [3, 8, 12, 5, 10, 7]

# Calculates the sum of numbers strictly greater than 6.
# Counts how many numbers qualify.
# Calculates their average.
# Prints the average.
# Handles the possibility that no numbers qualify, without dividing by zero. In that case, print 0.

total = 0
count = 0
for num in numbers:
    if num > 6:
        total += num
        count += 1
if count == 0:
    print(0)
else:
    print(total / count)