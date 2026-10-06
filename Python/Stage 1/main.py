numbers = []
total = 0
largest = None
smallest = None
even_count = 0
odd_count = 0

while True:
    num = input("Enter a number: ")

    if num == "done":
        break

    try:  
        num = int(num)
    
    except ValueError:
        print("Must enter a number.")
        continue

    numbers.append(num)
    total += num

    if largest is None or num > largest:
        largest = num

    if smallest is None or num < smallest:
        smallest = num

    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

count = len(numbers)

print(numbers)
print("Numbers entered:", count)
print("Sum:", total)

if count > 0:
    average = total / count
    print("Average:", average)
    print("Largest:", largest)
    print("Smallest:", smallest)
    print("Even Count:", even_count)
    print("Odd Count:", odd_count)
else:
    print("Average: No numbers entered")
    print("Largest: No numbers entered")
    print("Smallest: No numbers entered")
    print("Even Count: No numbers entered")
    print("Odd Count: No numbers entered")