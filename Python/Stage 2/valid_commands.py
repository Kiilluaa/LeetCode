# You are given a string commands containing only the characters X, Y, Z, x, y, and z.
# Uppercase letters represent the beginning of a command, while lowercase letters represent its end.
# Each opening command must be closed by its matching lowercase character:
# - X matches x
# - Y matches y
# - Z matches z
# Commands must close in the reverse order they were opened.
# Return True if all commands are properly matched and nested. Otherwise, return False.
# An empty string is considered valid.

def valid_commands(commands):
    stack = []
    matching = {
        "x": "X",
        "y": "Y",
        "z": "Z"
    }

    for i in commands:
        if i in "XYZ":
            stack.append(i)
        elif stack:
            if stack[-1] != matching[i]:
                return False
            stack.pop()
        else:
            return False
    return not stack

print(valid_commands("XYyx"))      # Expected: True
print(valid_commands("XYxy"))      # Expected: False
print(valid_commands("XYZzyx"))    # Expected: True
print(valid_commands("XxYy"))      # Expected: True
print(valid_commands("XXxx"))      # Expected: True
print(valid_commands("XYYyxx"))    # Expected: False
print(valid_commands("xX"))        # Expected: False
print(valid_commands("XYZ"))       # Expected: False
print(valid_commands(""))          # Expected: True
print(valid_commands("Xy"))        # Expected: False