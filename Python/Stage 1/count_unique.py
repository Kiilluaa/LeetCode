# Return how many unique values are in the sorted list.

def count_unique(nums):
    if not nums:
        return 0

    count = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            count += 1
    return count

print(
    count_unique([1, 1, 2, 2, 3]),   # 3
    count_unique([4, 4, 4]),         # 1
    count_unique([])                # 0
)