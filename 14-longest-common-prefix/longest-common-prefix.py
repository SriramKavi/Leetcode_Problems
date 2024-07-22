class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        n = len(strs[0])
        s = ''
        if strs[0] == "" or strs[-1] == "":
            return ""
        for i in range(n):
            if strs[0][i] == strs[-1][i]:
                s += strs[0][i]
            else:
                return s
        return s