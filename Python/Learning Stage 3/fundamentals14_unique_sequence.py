# Given a string s, return the length of the longest contiguous 
# sequence of characters that contains no repeated characters.


def longest_unique_sequence(s):
    seen = {}
    left = 0
    longest = 0

    for i in range(len(s)):
        seen[s[i]] = seen.get(s[i], 0) + 1

        while max(seen.values()) > 1:
            seen[s[left]] = seen.get(s[left], 0) - 1
            if seen.get(s[left]) == 0:
                del seen[s[left]]
            left += 1
        longest = max(longest, i - left + 1)
    return longest
        
def longest_unique_sequence(s):
    seen = {}
    left = 0
    longest = 0

    for right in range(len(s)):
        char = s[right]
        seen[char] = seen.get(char, 0) + 1

        while seen[char] > 1:
            seen[s[left]] -= 1

            if seen[s[left]] == 0:
                del seen[s[left]]

            left += 1

        longest = max(longest, right - left + 1)

    return longest

print(longest_unique_sequence("abcabcbb"))  # Expected: 3
print(longest_unique_sequence("bbbbb"))     # Expected: 1
print(longest_unique_sequence("pwwkew"))    # Expected: 3
print(longest_unique_sequence(""))          # Expected: 0
print(longest_unique_sequence("abcdef"))    # Expected: 6
print(longest_unique_sequence("abba"))      # Expected: 2
print(longest_unique_sequence("dvdf"))      # Expected: 3
