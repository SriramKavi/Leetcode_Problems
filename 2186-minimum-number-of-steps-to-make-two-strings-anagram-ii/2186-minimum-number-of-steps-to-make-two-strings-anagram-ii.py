class Solution:
    def minSteps(self, s: str, t: str) -> int:
        a = [0] * 26
        b = [0] * 26
        for i in s:
            a[ord(i) - 97] += 1
        for i in t:
            b[ord(i) - 97] += 1
        c = 0
        for i in range(26):
            c += abs(a[i] - b[i])
        return c