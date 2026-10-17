# Given a list of distinct strings, return every possible ordering of those strings.

class Solution(object):
    def permuteWords(self, words):
        result = []
        path = []

        def backtrack():
            if len(path) == len(words):
                result.append(path.copy())
                return

            for i in range(len(words)):
                if words[i] in path:
                    continue

                path.append(words[i])
                backtrack()
                path.pop()

        backtrack()
        return result