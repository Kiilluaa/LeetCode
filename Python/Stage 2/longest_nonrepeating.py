# Given a string s, return the length of the longest contiguous substring that contains no repeated characters.

def length_of_longest_substring(s):
    left = 0
    seen = set()
    longest = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])

        if len(seen) > longest:
            longest = len(seen)

    return longest