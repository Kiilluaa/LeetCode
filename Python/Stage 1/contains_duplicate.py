# Return True if any value appears at least twice.
# Return False if every value is unique.

def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        
        seen.add(num)
    return False

print(
    contains_duplicate([1, 2, 3, 1]),   # True
    contains_duplicate([1, 2, 3, 4])   # False
)