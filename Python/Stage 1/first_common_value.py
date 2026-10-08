# You are given two sorted integer lists.
# Return the first value that appears in both lists.
# If there is no common value, return -1.

def first_common_value(nums1, nums2):
    p1 = 0
    p2 = 0

    while p1 < len(nums1) and p2 < len(nums2):
        if nums1[p1] == nums2[p2]:
            return nums1[p1]
        elif nums1[p1] > nums2[p2]:
            p2 += 1
        else:
            p1 += 1

    return -1

print(first_common_value([1, 4, 6], [2, 3, 5]))

# nums1 = [1, 3, 5, 7]
# nums2 = [2, 3, 6, 8]

# # Return:
# 3

# nums1 = [1, 4, 6]
# nums2 = [2, 3, 5]

# # Return:
# -1