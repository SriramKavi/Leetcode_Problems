class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        a = arr.copy()
        a.sort()
        d = {}
        p = 1
        for i in a:
            if i not in d:
                d[i] = p
                p += 1
            else:
                d[i] = p - 1
        res = []
        for i in arr:
            res.append(d[i])
        return res
        
