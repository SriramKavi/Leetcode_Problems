class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = 0
        c = 0
        i = 0
        k = []
        while i < len(s):
            if s[i] in k:
                while s[i] in k:
                    k.pop(0)
                k += s[i]
            else:
                k += [s[i]]
                c = len(k)
                if c > m:
                    m = c
            i += 1
        return m