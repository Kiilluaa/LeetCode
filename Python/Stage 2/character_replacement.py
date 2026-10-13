def character_replacement(s, k):
    left = 0
    counts = {}
    longest = 0

    for right in range(len(s)):
        counts.get(s[right], 0) + 1

        # 2. Shrink while replacements needed > k
        
        # 3. Update longest

    return longest