# Given a list of strings strs, group together all strings that are anagrams of one another.
# Two strings are anagrams if they contain the same characters with the same frequencies, regardless of order.
# Your function must return a list of lists, where each inner list contains strings that are anagrams of each other.


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = {}

        for word in strs:
            letters = sorted(word)
            key = tuple(letters)
            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        result = list((groups.values()))
        return result


sol = Solution()

print(sol.groupAnagrams(
    ["eat", "tea", "tan", "ate", "nat", "bat"]
))
# Expected groups:
# [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

print(sol.groupAnagrams([""]))
# Expected: [[""]]

print(sol.groupAnagrams(["a"]))
# Expected: [["a"]]

print(sol.groupAnagrams(["abc", "bca", "cab", "xyz", "zyx"]))
# Expected groups:
# [["abc", "bca", "cab"], ["xyz", "zyx"]]

print(sol.groupAnagrams(["a", "b", "a"]))
# Expected groups:
# [["a", "a"], ["b"]]
