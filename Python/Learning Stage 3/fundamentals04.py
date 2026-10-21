numbers = [4, 7, 3, 9, 6]

# Write code that counts how many times an element is strictly greater than the element immediately before it.

count = 0
for i in range(len(numbers) - 1):
    if numbers[i + 1] > numbers[i]:
        count += 1
print(count)