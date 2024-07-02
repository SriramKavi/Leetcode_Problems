class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        m = 0
        i = 0
        k = []
        while i < n:
            while s[i] in k:
                k.pop(0)
            k += s[i]
            m = max(m, len(k))
            i += 1
        return m