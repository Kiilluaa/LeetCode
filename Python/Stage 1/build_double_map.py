# Use each number as the key.
# Store double that number as the value.

def build_double_map(nums):
    double = {}
    for num in nums:
        double[num] = num * 2
    return double

print(build_double_map([2, 5, 7]))