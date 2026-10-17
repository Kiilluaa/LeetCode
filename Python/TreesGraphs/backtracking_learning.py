# # Choose — Add something to our current solution.
# # Explore — Recursively continue building that solution.
# # Undo — Remove our choice so we can explore another possibility.

# # EX. Generating Combinations
# nums = [1, 2, 3]
# # We want every combination containing exactly two numbers.
# #Expected Return
# [[1, 2], [1, 3], [2, 3]]

# # []
# # |- [1] - [1,2]
# # |   |- [1,3]
# # |
# # |- [2] - [2,3]

# # We might write:
# path = []
# path.append(1) # [1]
# path.append(2) # [1,2]

# # Now we've completed one combination. To explore [1, 3], we need to remove 2 first.
# path = []

# path.append(1)
# path.append(2)
# path.pop()
# path.append(3)

class Solution(object):
    def combine(self, nums):
        result = [] # store completed combinations
        path = [] # stores the combination currently building
        
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

