class Solution(object):
    def permute(self, nums):
        result = []
        path = []

        def backtrack():
            if len(path) == len(nums):
                result.append(path.copy())
                return

            for i in range(len(nums)):
                if nums[i] in path:
                    continue

                path.append(nums[i])
                backtrack()
                path.pop()

        backtrack()
        return result