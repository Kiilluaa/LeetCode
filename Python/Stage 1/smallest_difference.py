# Given two sorted integer lists, return the smallest absolute 
# difference between any value from nums1 and any value from nums2.

def smallest_difference(nums1, nums2):
    p1 = 0
    p2 = 0
    smallest = None

    while p1 < len(nums1) and p2 < len(nums2):
        difference = abs(nums1[p1] - nums2[p2])

        if difference == 0:
            return difference

        if smallest is None or difference < smallest:
            smallest = difference
        if nums1[p1] > nums2[p2]:
            p2 += 1
        else:
            p1 += 1
    return smallest

print(smallest_difference([1, 4, 10], [2, 15, 20]))
print(smallest_difference([5, 8, 12], [3, 9, 14]))


# nums1 = [1, 4, 10]
# nums2 = [2, 15, 20]

# # Return:
# 1

# nums1 = [5, 8, 12]
# nums2 = [3, 9, 14]

# # Return:
# 1