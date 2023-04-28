from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float("-inf")
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            if total > ans:
                ans = total
            if total < 0:
                total = 0
        return ans
