class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        d1 = {}
        d2 = {}
        for i in matches:
            if i[0] in d1:
                d1[i[0]] += 1
            else:
                d1[i[0]] = 1
        for i in matches:
            if i[1] in d2:
                d2[i[1]] += 1
            else:
                d2[i[1]] = 1
        p = []
        q = []
        for i in d1:
            if i not in d2:
                p += [i]
        for a, b in d2.items():
            if b == 1:
                q += [a]
        p.sort()
        q.sort()
        return [p, q]
            
        