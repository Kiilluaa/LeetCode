# Return the value that appears the most times.
# If multiple values tie, return the one that appears first in the original list.

def most_frequent(nums):
    frequency = {}
    if not nums:
        return -1
    
    for num in nums:
        if num not in frequency:
            frequency[num] = 1
        else:
            frequency[num] += 1

    val = 0
    number = 0
    for num in nums:
        if frequency[num] > val:
            val = frequency[num]
            number = num

    return number

print(most_frequent([4, 2, 4, 3, 2, 4]))