import math
# temperatures = [75, 71, 69, 72]
# stack = [0, 1, 2]

# # print("Before:", stack)

# # while stack and temperatures[3] > temperatures[stack[-1]]:
# #     previous = stack.pop()
# #     print("Resolved day:", previous)
# #     print("Stack now:", stack)


# print(temperatures.pop(-1))
piles = [1,4,3,2]
h = 9
total = sum(piles)
hi = h / total
print(h / total)
while hi < 1:
    h += 1
    hi = h / total
print(h)