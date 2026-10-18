# Given a list of integers, return the k numbers with the smallest absolute values, ordered by increasing absolute value.
# Assume no two numbers have the same absolute value.

import heapq

class Solution(object):
    def kSmallestAbsolute(self, nums, k):
        increasing = []
        new = [(abs(num), num) for num in nums]
        heapq.heapify(new)

        while len(increasing) < k:
            priority, original = heapq.heappop(new)
            increasing.append(original)

        return increasing