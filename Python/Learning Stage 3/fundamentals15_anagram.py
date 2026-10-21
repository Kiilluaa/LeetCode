
def are_anagrams(s, t):
    if len(s) != len(t):
        return False
    
    frequency1 = {}
    frequency2 = {}
    
    for i in range(len(s)):
        frequency1[s[i]] = frequency1.get(s[i], 0) + 1
        frequency2[t[i]] = frequency2.get(t[i], 0) + 1

    # print(frequency1)
    # print(frequency2)
    if frequency1 == frequency2:
        return True
    return False


print(are_anagrams("listen", "silent"))
# Expected: True

print(are_anagrams("aab", "abb"))
# Expected: False

print(are_anagrams("anagram", "nagaram"))
# Expected: True

print(are_anagrams("rat", "car"))
# Expected: False

print(are_anagrams("", ""))
# Expected: True

print(are_anagrams("abc", "abcd"))
# Expected: False

print(are_anagrams("aabbcc", "abcabc"))
# Expected: True
