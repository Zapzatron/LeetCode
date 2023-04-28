from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(line, left, right, ans=[]):
            if left:
                generate(line + '(', left - 1, right)
            if right > left:
                generate(line + ')', left, right - 1)
            if not right:
                ans += line,
            return ans
        return generate('', n, n)