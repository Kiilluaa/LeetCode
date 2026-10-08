# You are given two sorted integer lists.
# Return a new list containing the values that appear in both lists.
# Each matching position can only be used once.

def common_values(nums1, nums2):
    common = []
    p1 = 0
    p2 = 0

    while p1 < len(nums1) and p2 < len(nums2):
        if nums1[p1] == nums2[p2]:
            common.append(nums1[p1])
            p1 += 1
            p2 += 1
        elif nums1[p1] > nums2[p2]:
            p2 += 1
        else:
            p1 += 1
    return common

print(common_values([1, 3, 5, 7], [2, 3, 5, 8]))
# nums1 = [1, 3, 5, 7]
# nums2 = [2, 3, 5, 8]

# # Return:
# [3, 5]

# nums1 = [1, 2, 2, 4]
# nums2 = [2, 2, 3, 4]

# # Return:
# [2, 2, 4]