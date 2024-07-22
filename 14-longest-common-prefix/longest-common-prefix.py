class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        n = len(strs[0])
        s = ''
        a, b = strs[0], strs[-1]
        for i in range(n):
            if a[i] != b[i]:
                return s
            s += a[i]
        return s