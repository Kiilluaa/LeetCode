# Given a lowercase string text, determine whether the string is already a palindrome or can become a
# palindrome after removing at most one character.
# Return
# Return True if it can be a palindrome after removing zero or one character. Otherwise return False.


def almost_palindrome(text):

    def is_palindrome_range(left, right):
        while left < right:
            if text[left] != text[right]:
                return False

            left += 1
            right -= 1

        return True

    left = 0
    right = len(text) - 1

    while left < right:
        if text[left] == text[right]:
            left += 1
            right -= 1
        else:
            return (
                is_palindrome_range(left + 1, right)
                or
                is_palindrome_range(left, right - 1)
            )

    return True


print(almost_palindrome("abca"))
print(almost_palindrome("abcdef"))