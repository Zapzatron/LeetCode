class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len_str = 0
        n = len(s)
        for i in range(n):
            cur_len_str = 0
            cur_str = s[i]
            while True:
                try:
                    if s[i + 1] not in cur_str:
                        cur_str = cur_str + s[i + 1]
                        # print(i, i + 1, cur_str)
                    else:
                        if max_len_str < len(cur_str):
                            max_len_str = len(cur_str)
                        break
                    i += 1
                except IndexError:
                    if max_len_str < len(cur_str):
                        max_len_str = len(cur_str)
                    break
        # print(max_len_str)
        return max_len_str
