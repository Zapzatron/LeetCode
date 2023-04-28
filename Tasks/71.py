import os.path


class Solution:
    def simplifyPath(self, path: str) -> str:
        return os.path.realpath(path)
