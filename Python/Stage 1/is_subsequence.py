# You are given two strings s and t.
# Return True if s is a subsequence of t. Otherwise return False.
# A subsequence means the characters of s appear in t in the same order, but they do not need to be next to each other.

def is_subsequence(s, t):
    if not s:
        return True
    
    pointer1 = 0
    pointer2 = 0

    while pointer2 < len(t):
        if s[pointer1] == t[pointer2]:
            pointer1 += 1

        pointer2 += 1

        if pointer1 == len(s):
            return True

    return False

print(is_subsequence("abc", "ahbgdc"))
print(is_subsequence("axc", "ahbgdc"))

# Input: s = "abc", t = "ahbgdc"
# Output: True

# Input: s = "axc", t = "ahbgdc"
# Output: False