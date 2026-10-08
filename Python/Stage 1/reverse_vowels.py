# Given a string text, return a new string where only the vowels are reversed. All non-vowel characters must
# remain in their original positions. Treat a, e, i, o, u as vowels. The input will contain lowercase letters only.
# Return
# Return the resulting string after reversing only the vowels

def reverse_vowels(text):
    chars = list(text)
    left = 0
    right = len(chars) - 1

    while left < right:
        if chars[left] not in ["a", "e", "i", "o", "u"]:
            left += 1
        elif chars[right] not in ["a", "e", "i", "o", "u"]:
            right -= 1
        else:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1

    return "".join(chars)

print(reverse_vowels("alle"))
print(reverse_vowels("hello"))
print(reverse_vowels("leetcode"))