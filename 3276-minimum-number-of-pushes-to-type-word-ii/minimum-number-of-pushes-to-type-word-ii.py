class Solution:
    def minimumPushes(self, s: str) -> int:
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        p = sorted(list(d.values()), reverse = True)
        k = 1
        i = 1
        ans = p[0]
        while i < len(p):
            if i % 8 == 0:
                k += 1
            ans += p[i] * k
            i += 1
        return ans