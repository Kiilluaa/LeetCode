# Given a list of distinct integers, return every combination 
# containing exactly three numbers, preserving their original order.

class Solution(object):
    def generateTriplets(self, nums):
        result = []
        path = []

        def backtrack(start):
            if len(path) == 3:
                result.append(path.copy())
                return

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()

        backtrack(0)
        return result