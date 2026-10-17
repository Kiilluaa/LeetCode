# Given a list of distinct integers, return every possible combination of exactly two numbers.
# Each combination must preserve the order of the original list, and reversed combinations should not be repeated.

class Solution(object):
    def generatePairs(self, nums):
        result = []
        path = []

        def backtrack(start):
            if len(path) == 2:
                result.append(path.copy())
                return

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()

        backtrack(0)
        return result