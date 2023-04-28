from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_left, max_right, ans = height[left], height[right], 0

        while left < right:
            if max_left < max_right:
                ans += max_left - height[left]
                left += 1
                max_left = max(height[left], max_left)
            else:
                ans += max_right - height[right]
                right -= 1
                max_right = max(height[right], max_right)
        return ans