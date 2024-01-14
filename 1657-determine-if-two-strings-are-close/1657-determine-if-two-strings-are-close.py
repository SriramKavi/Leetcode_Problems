class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        d1 = {}
        d2 = {}
        for i in word1:
            if i in d1:
                d1[i] += 1
            else:
                d1[i] = 1
        for i in word2:
            if i in d2:
                d2[i] += 1
            else:
                d2[i] = 1
        a = list(d1.keys())
        b = list(d2.keys())
        c = list(d1.values())
        d = list(d2.values())
        a.sort()
        b.sort()
        c.sort()
        d.sort()
        if a == b and c == d:
            return True
        return False
        