class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        m = max(list(d.values()))
        l = [[] for _ in range(m)]
        for k, v in d.items():
            if v - 1 >= 0:
                v = v - 1
                while v >= 0:
                    l[v].append(k)
                    v = v - 1
        return l
                   
            
        