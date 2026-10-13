def remove_duplicates(s):
    stack = []

    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return "".join(stack)

print(remove_duplicates("abbaca"))  # Expected: ca
print(remove_duplicates("azxxzy"))  # Expected: ay
print(remove_duplicates("aaaa"))    # Expected: ""
print(remove_duplicates("abc"))     # Expected: abc
print(remove_duplicates(""))        # Expected: ""