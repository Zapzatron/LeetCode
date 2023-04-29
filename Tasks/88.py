from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # print(nums1)
        for i in range(1, n + 1):
            # print(i)
            nums1[-i] = nums2[-i]
        # print(nums1)

        nums1.sort()
