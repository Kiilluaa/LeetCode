numbers = [2, 4, 6, 8, 10]

# Write code that uses two pointers to print pairs of numbers, starting from opposite ends of the list and moving inward.

left = 0
right = len(numbers) - 1

while left < right:
    print([numbers[left], numbers[right]])
    left += 1
    right -= 1