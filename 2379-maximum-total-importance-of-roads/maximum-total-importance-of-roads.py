class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        d = {}
        for city in roads:
            if city[0] in d and city[1] not in d:
                d[city[0]] += 1
                d[city[1]] = 1
            elif city[1] in d and city[0] not in d:
                d[city[1]] += 1
                d[city[0]] = 1
            elif city[0] in d and city[1] in d:
                d[city[0]] += 1
                d[city[1]] += 1
            else:
                d[city[0]] = 1
                d[city[1]] = 1
        lst = sorted(d.items(), key = lambda x: (x[1], x[0]), reverse = True)
        res = [0] * n
        p = n
        for i in lst:
            res[i[0]] = p
            p -= 1
        ans = 0
        for cit in roads:
            ans += res[cit[0]] + res[cit[1]]
        return ans