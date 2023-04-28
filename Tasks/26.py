from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        default = 200
        if n < default:
            n = n // 2
        else:
            n = n // (n // default)
        count = 0
        while True:
            if count == n:
                break
            for num in nums:
                if nums.count(num) > 1:
                    nums.remove(num)
            count += 1

        # print(count)
        # print(nums)
        return len(nums)
