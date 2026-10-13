# Given a string containing only the characters A, B, C, a, b, and c, determine whether the tags are correctly nested.
# Uppercase characters represent opening tags, and their lowercase counterparts represent closing tags.
# For example:
# - A opens a tag, and a closes it.
# - B opens a tag, and b closes it.
# - C opens a tag, and c closes it.
# The most recently opened tag must be closed first.

def valid_tags(s):
    stack = []
    matching = {
        "a": "A",
        "b": "B",
        "c": "C"
    }

    for i in s:
        if i in "ABC":
            stack.append(i)
        elif stack:
            if stack[-1] != matching[i]:
                return False
            stack.pop()
        else:
            return False
    return not stack

print(valid_tags("ABba"))    # Expected: True
print(valid_tags("ABab"))    # Expected: False
print(valid_tags("ABCcba"))  # Expected: True
print(valid_tags("AaBb"))    # Expected: True
print(valid_tags("Aab"))     # Expected: False
print(valid_tags("aA"))      # Expected: False
print(valid_tags("AAaa"))    # Expected: True
print(valid_tags(""))        # Expected: True