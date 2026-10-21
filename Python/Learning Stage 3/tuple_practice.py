# Given a list of integers nums, return the number that appears most frequently.
# If multiple numbers have the same highest frequency, return the smallest number among them.

# Before writing any code, answer these three questions in your own words:
# 1. What information do you need to track to determine which number appears most frequently?
# 2. What data structure would you choose, and why?
# 3. How would you handle a tie between two numbers with equal frequencies?

# 1. we need to track the frequency of each integer in nums
# 2. use a frequency dictionary because you can track the number of appearances of each element
# 3. for a tie we need to return the smallest number that has the same highest frequency

# def max_frequency(nums):
#     best_num = None
#     highest_freq = 0
#     freq = {}

#     for num in nums:
#         freq[num] = freq.get(num, 0) + 1

#     for num, frequency in freq.items():
#         if frequency > highest_freq:
#             best_num = num
#             highest_freq = frequency
#         elif frequency == highest_freq and num < best_num:
#             best_num = num
#     return best_num


def majority_element(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    for num, frequency in freq.items():
        if frequency > (len(nums) / 2):
            return num

print(majority_element([3, 2, 3]))        # 3
print(majority_element([2, 2, 1, 1, 1, 2, 2]))  # 2
print(majority_element([5]))              # 5
print(majority_element([4, 4, 4, 2, 2]))  # 4