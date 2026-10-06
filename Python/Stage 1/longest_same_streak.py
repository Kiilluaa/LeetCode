# Return the length of the longest streak of identical consecutive numbers.

def longest_same_streak(nums):
    if not nums:
        return 0
    
    streak = 1
    longest_streak = 1

    for i in range(len(nums) - 1):
        if nums[i] == nums[i+1]:
            streak += 1
        else:
            streak = 1

        if streak > longest_streak:
            longest_streak = streak
    return longest_streak

print(longest_same_streak([1, 1, 2, 2, 2, 3, 3]))