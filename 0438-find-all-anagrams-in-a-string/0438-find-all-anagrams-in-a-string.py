class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = "".join(sorted(p))
        i = 0
        res = []
        while i <= len(s) - len(p):
            if "".join(sorted(s[i:len(p) + i])) == k:
                res += [i]
            i += 1
        return res
        