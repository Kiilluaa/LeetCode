# return the length of the longest consecutive run of positive numbers

def longest_positive_streak(nums):
    streak = 0
    longest_streak = 0
    for num in nums:
        if num > 0:
            streak += 1
        else:
            streak = 0
        if streak > longest_streak:
            longest_streak = streak
    return longest_streak

print(longest_positive_streak([1, 2, -3, 4, 5, 6, -1, 2]))