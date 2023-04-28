from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            num_1 = nums[i]
            for j in range(len(nums)):
                if i != j:
                    num_2 = nums[j]
                    if (num_1 + num_2) == target:
                        return [i, j]
