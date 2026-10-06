# Return the first value that appears a second time while scanning left to right.
# If no duplicate exists, return -1.

def first_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return -1

print(first_duplicate([2, 1, 3, 5, 3, 2]))