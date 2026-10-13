def is_valid(s):
    stack = []
    matching = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for i in s:
        if i in "([{":
            stack.append(i)
        elif stack:
            if stack[-1] != matching[i]:
                return False
            stack.pop()
        else:
            return False

    return not stack

print(is_valid("()"))    # Expected: True
print(is_valid("([{}])")) # Expected: True
print(is_valid("([)]"))  # Expected: False
print(is_valid(")"))     # Expected: False
print(is_valid("(("))    # Expected: False
print(is_valid(""))      # Expected: True