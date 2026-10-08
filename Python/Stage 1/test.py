def intersection(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    intersection = set()
    p1 = 0
    p2 = 0

    nums1.sort()
    print(nums1)
    # while p1 < len(nums1) and p2 < len(nums2):
    #     if nums1[p1] == nums2[p2]:
    #         intersection.add(nums1[p1])
    #         p1 += 1
    #         p2 += 1
    #     else:

print(intersection([1,2,2,1], [2,2]))