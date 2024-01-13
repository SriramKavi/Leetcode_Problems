class Solution:
    def minSteps(self, s: str, t: str) -> int:
        a = [0] * 26
        b = [0] * 26
        for i in s:
            a[ord(i) - 97] += 1
        for i in t:
            b[ord(i) - 97] += 1
        res = 0
        for i in range(len(a)):
            if a[i] >= b[i]:
                res += (a[i] - b[i])
        return res
            