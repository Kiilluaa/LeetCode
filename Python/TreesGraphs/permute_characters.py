# Given a string containing distinct characters, return all possible permutations as a list of strings, not a list of lists.

class Solution(object):
    def permuteChars(self, s):
        result = []
        path = []

        def backtrack():
            if len(path) == len(s):
                completed = path.copy()
                result.append("".join(completed))
                return

            for char in range(len(s)):
                if s[char] in path:
                    continue

                path.append(s[char])
                backtrack()
                path.pop()
        
        backtrack()
        return result