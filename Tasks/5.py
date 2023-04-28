class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_str = ""
        n = len(s)

        if s == s[::-1]:
            return s

        for i in range(n):
            for j in range(i, n + 1):
                cur_str = s[i:j]
                if cur_str == cur_str[::-1] and len(max_str) < len(cur_str):
                    max_str = cur_str

        return max_str
