# Return a dictionary where each number maps to how many times it appears.

def frequency_count(nums):
    frequency = {}
    for num in nums:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    return frequency

print(frequency_count([2, 2, 3, 2, 5, 3]))