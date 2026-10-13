# You are given a list of strings called operations, representing actions performed in a simple text editor.
# Each operation is one of the following:
# - A single lowercase letter ("a" through "z"): Add that letter to the end of the text.
# - "UNDO": Remove the most recently added letter that hasn't already been removed.
# - "DOUBLE": Add another copy of the most recently added letter.
# Return the final text as a string after processing all operations.
# You may assume that "UNDO" and "DOUBLE" are only used when there is at least one letter available.

def process_editor(operations):
    stack = []

    for i in operations:
        if i == "DOUBLE":
            stack.append(stack[-1])
        elif i == "UNDO":
            stack.pop()
        else:
            stack.append(i)
    return "".join(stack)

print(process_editor(["a", "b", "UNDO", "c", "DOUBLE"]))  # Expected: "acc"
print(process_editor(["x", "y", "DOUBLE", "UNDO", "z"]))  # Expected: "xyz"
print(process_editor(["a", "DOUBLE", "DOUBLE"]))         # Expected: "aaa"
print(process_editor(["a", "b", "UNDO", "UNDO"]))         # Expected: ""
print(process_editor(["m", "n", "o"]))                    # Expected: "mno"
print(process_editor([]))                               # Expected: ""
print(process_editor(["a", "UNDO", "b"]))                # Expected: "b"
print(process_editor(["q", "DOUBLE", "UNDO"]))          # Expected: "q"