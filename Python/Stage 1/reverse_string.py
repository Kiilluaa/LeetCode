# You are given a list of characters s. Reverse the list in place.
# You must modify the original list and use O(1) extra memory.
# Return:
# Return s after it has been reversed for our practice version. On actual LeetCode 344, 
# the function modifies the list and does not return the reversed list.

def reverse_string(s):
    left = 0
    right = len(s) - 1

    while left < right:
        current = s[left]
        s[left] = s[right]
        s[right] = current

        left += 1
        right -= 1
    return s

print(reverse_string(["h", "e", "l", "l", "o"]))
# Input: s = ["h", "e", "l", "l", "o"]

# Output:
# ["o", "l", "l", "e", "h"]