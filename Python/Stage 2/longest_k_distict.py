# This is almost identical to the problem you just completed, 
# except the maximum number of distinct characters is no longer fixed at 2.
# Goal: Return the length of the longest contiguous substring containing at most k distinct characters.

def longest_k_distinct(s, k):
    left = 0
    counts = {}
    longest = 0

    for right in range(len(s)):
        counts[s[right]] = counts.get(s[right], 0) + 1

        while len(counts) > k:
            counts[s[left]] -= 1

            if counts[s[left]] == 0:
                del(counts[s[left]])

            left += 1

        longest = max(right - left + 1, longest)

    return longest

print(longest_k_distinct("eceba", 2))    # 3
print(longest_k_distinct("aaabbcc", 2))  # 5
print(longest_k_distinct("abc", 1))      # 1
print(longest_k_distinct("aaaa", 0))     # 0
print(longest_k_distinct("", 2))        # 0