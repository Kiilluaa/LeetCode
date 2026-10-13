# Given a string symbols containing only P, Q, R, p, q, and r, determine whether all opening and closing symbols are properly matched.
# Uppercase letters represent opening symbols. Their lowercase equivalents are closing symbols.
# Symbols must close in the reverse order they were opened.
# Return True if the string is valid; otherwise return False.
# An empty string is valid.

def valid_symbols(symbols):
    stack = []
    matching = {
        "p": "P",
        "q": "Q",
        "r": "R"
    }

    for i in symbols:
        if i in "PQR":
            stack.append(i)
        elif stack:
            if stack[-1] != matching[i]:
                return False
            stack.pop()
        else:
            return False
    return not stack

print(valid_symbols("PQqp"))      # Expected: True
print(valid_symbols("PQRrqp"))    # Expected: True
print(valid_symbols("PQpq"))      # Expected: False
print(valid_symbols("PpQq"))      # Expected: True
print(valid_symbols("PPpp"))      # Expected: True
print(valid_symbols("pPp"))       # Expected: False
print(valid_symbols("PQR"))       # Expected: False
print(valid_symbols("Pq"))        # Expected: False
print(valid_symbols(""))          # Expected: True
print(valid_symbols("p"))         # Expected: False