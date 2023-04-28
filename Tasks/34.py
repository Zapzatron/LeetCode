from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # print(nums, target)
        # print(nums.index(target))
        ans = [0, 0]
        try:
            ans[0] = nums.index(target)
        except ValueError:
            return [-1, -1]
        nums = nums[::-1]
        ans[1] = len(nums) - 1 - nums.index(target)
        # print(nums)
        # print(len(nums) - 1 - nums.index(target))
        return ans
