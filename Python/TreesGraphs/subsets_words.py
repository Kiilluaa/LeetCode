# Given a list of distinct strings, return all possible subsets, including the empty subset.

class Solution(object):
    def subsetsWords(self, words):
        result = []
        path = []

        def backtrack(start):
            result.append(path.copy())

            for i in range(start, len(words)):
                path.append(words[i])
                backtrack(i + 1)
                path.pop()

        backtrack(0)
        return result