# You are given two integer arrays nums1 and nums2, both sorted in ascending order.
# Count how many values appear in both arrays.
# Each matching position may only be used once.
# Return:
# Return the number of matches.

def count_matching_pairs(nums1, nums2):
    arr1 = 0
    arr2 = 0
    count = 0

    while arr1 < len(nums1) and arr2 < len(nums2):
        if nums1[arr1] < nums2[arr2]:
            arr1 += 1
        elif nums1[arr1] > nums2[arr2]:
            arr2 += 1
        else:
            arr1 += 1
            arr2 += 1
            count += 1
    return count

print(count_matching_pairs([1, 3, 5, 7], [2, 3, 5, 8]))
# nums1 = [1, 3, 5, 7]
# nums2 = [2, 3, 5, 8]

# # Return: 2

# nums1 = [1, 2, 4]
# nums2 = [2, 3, 4, 6]

# # Return: 2