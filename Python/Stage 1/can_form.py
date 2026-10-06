# Return True if every character in word can be matched in source in the same order.
# The characters do not need to be adjacent.
# Return:
# - True if word can be formed as a subsequence of source
# - otherwise False

def can_form(word, source):
    if not word:
        return True

    p1 = 0
    p2 = 0

    while p2 < len(source):
        if word[p1] == source[p2]:
            p1 += 1

        p2 += 1

        if p1 == len(word):
            return True

    return False

print(can_form("ace", "abcde"))
print(can_form("aec", "abcde"))