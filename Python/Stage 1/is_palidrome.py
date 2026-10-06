# Return True if text reads the same forward and backward, otherwise return False

def is_palindrome(text):
    left = 0
    right = len(text) - 1
    while left < right:
            if text[left] == text[right]:
                left += 1
                right -= 1
            else:
                return False
    return True
        

print(
    is_palindrome("racecar"),   # True
    is_palindrome("level"),     # True
    is_palindrome("hello")     # False
)