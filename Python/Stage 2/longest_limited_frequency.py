# Given a string s and an integer k, return the length of the longest 
# contiguous substring in which no character appears more than k times.
# A substring is a continuous sequence of characters within a string.

def longest_limited_frequency(s, k):
    left = 0
    counts = {}
    longest = 0

    for right in range(len(s)):
        counts[s[right]] = counts.get(s[right], 0) + 1

        while counts and max(counts.values()) > k:
            counts[s[left]] -= 1

            if counts[s[left]] == 0:
                del(counts[s[left]])

            left += 1
        longest = max(longest, right - left + 1)

    return longest

        

print(longest_limited_frequency("aabbcc", 2))  # 6
print(longest_limited_frequency("aaabbc", 2))  # 5
print(longest_limited_frequency("abcabc", 1))  # 3
print(longest_limited_frequency("aaaa", 1))    # 1
print(longest_limited_frequency("aabbaa", 2))  # 4
print(longest_limited_frequency("abc", 0))     # 0
print(longest_limited_frequency("", 2))        # 0

# print(longest_limited_frequency("aaabbc", 2))  # Expected: 5
# print(longest_limited_frequency("abcabc", 1))  # Expected: 3
# print(longest_limited_frequency("abc", 0))     # Expected: 0