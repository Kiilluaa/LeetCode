# import heapq

# heap = [] # create a heap
# heapq.heappush(heap, 5) # add 5 while maintaining heap order
# heapq.heappop(heap) # remove and return the smallest value

# Example
# import heapq

# heap = []

# heapq.heappush(heap, 8)
# heapq.heappush(heap, 3)
# heapq.heappush(heap, 10)

# smallest = heapq.heappop(heap)

import heapq

heap = []

# heapq.heappush(heap, 8)
# heapq.heappush(heap, 3)
# heapq.heappush(heap, 10)
# heapq.heappush(heap, 1)
# heapq.heappush(heap, 6)

# smallest = heap[0]
# print(heap)

nums = [8, 3, 10, 1, 6]
heapq.heapify(nums)
heapq.heappop(nums)
print(nums)