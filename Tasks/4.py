from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for num in nums2:
            nums1.append(num)
        nums1.sort()
        # print(len(nums1) / 2)
        # print(len(nums1) // 2 )
        middle = len(nums1) // 2
        if (len(nums1)) % 2 == 0:
            # print(nums1[middle] + nums1[middle - 1])
            # print((nums1[middle] + nums1[middle - 1]) / 2)
            return (nums1[middle] + nums1[middle - 1]) / 2
        else:
            return nums1[middle]
