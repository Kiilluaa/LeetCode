# Given a list of integers and an integer k, return the k largest numbers in descending order.

import heapq

class Solution(object):
    def kLargest(self, nums, k):
        desc = []
        new = [-num for num in nums]
        heapq.heapify(new)

        while len(desc) < k:
            desc.append(heapq.heappop(new))

        desc = [-num for num in desc]
        return desc