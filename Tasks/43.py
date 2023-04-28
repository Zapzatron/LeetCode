class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def str_to_int(s):
            result = 0
            for char in s:
                result = result * 10 + (ord(char) - ord('0'))
            return result
        return str(str_to_int(num1) * str_to_int(num2))
