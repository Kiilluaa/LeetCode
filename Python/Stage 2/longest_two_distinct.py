def longest_two_distinct(s):
    left = 0
    counts = {}
    longest = 0

    for right in range(len(s)):
        counts[s[right]] = counts.get(s[right], 0) + 1

        while len(counts) > 2:
            counts[s[left]] -= 1

            if counts[s[left]] == 0:
                del(counts[s[left]])
            
            left += 1
        
        longest = max(right - left + 1, longest)

    return longest

print(longest_two_distinct("eceba"))
print(longest_two_distinct("aaaaa"))  # Expected: 5
print(longest_two_distinct("abc"))    # Expected: 2
print(longest_two_distinct(""))       # Expected: 0
print(longest_two_distinct("aabac"))  # Expected: 4