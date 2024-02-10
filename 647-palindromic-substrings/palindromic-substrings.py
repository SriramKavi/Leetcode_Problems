class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        pal_str = 0
        for i in range(n):
            for j in range(i, n):
                if s[i:j + 1] == s[i:j + 1][::-1]:
                    pal_str += 1
        return pal_str