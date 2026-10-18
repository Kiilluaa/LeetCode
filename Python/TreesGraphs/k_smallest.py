# Given a list of integers, return the k smallest numbers in ascending order.

import heapq

class Solution(object):
    def kSmallest(self, nums, k):
        asc = []
        new = nums.copy()
        heapq.heapify(new)

        while len(asc) < k:
            asc.append(heapq.heappop(new))
            
        return asc