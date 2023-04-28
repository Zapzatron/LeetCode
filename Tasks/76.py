class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        right = 0
        min_str = "A" * 99999
        char_count = {}
        for char in t:
            char_count[char] = char_count.get(char, 0) + 1
        required_chars = len(char_count)
        curr_chars = 0
        window_chars = {}
        while right < len(s):
            if s[right] in char_count:
                window_chars[s[right]] = window_chars.get(s[right], 0) + 1
                if window_chars[s[right]] == char_count[s[right]]:
                    curr_chars += 1
            right += 1
            while curr_chars == required_chars and left < right:
                if right - left < len(min_str):
                    min_str = s[left:right]
                if s[left] in window_chars:
                    window_chars[s[left]] -= 1
                    if window_chars[s[left]] < char_count[s[left]]:
                        curr_chars -= 1
                left += 1
        return min_str if len(min_str) <= len(s) else ""
