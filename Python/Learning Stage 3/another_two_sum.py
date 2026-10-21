# Given an array of integers nums and an integer target, return the indices of two different elements whose values add up to target.
# You may assume exactly one valid answer exists, and you cannot use the same element twice.


class Solution(object):
    def twoSum(self, nums, target):
        seen = {}

        for index, num in enumerate(nums):
            comp = target - num
            if comp in seen:
                return [seen[comp], index]
            seen[num] = index
            
        return -1 


sol = Solution()

print(sol.twoSum([2, 7, 11, 15], 9))   # Expected: [0, 1]
print(sol.twoSum([3, 2, 4], 6))         # Expected: [1, 2]
print(sol.twoSum([3, 3], 6))            # Expected: [0, 1]
print(sol.twoSum([-3, 4, 3, 90], 0))    # Expected: [0, 2]
print(sol.twoSum([1, 5, 8, 12], 13))    # Expected: [0, 3]
