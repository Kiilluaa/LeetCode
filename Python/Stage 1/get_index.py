# where is already a dictionary mapping numbers to indexes.
# Return the stored index for target.
# If target is not a key in the dictionary, return -1.
where = {
    8: 0,
    3: 1,
    7: 2
}

def get_index(where, target):
    if target in where:
        return where[target]

    return -1

print(get_index(where, 7))