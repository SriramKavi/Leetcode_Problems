class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        l = list(zip(list(d.values()), list(d.keys())))
        l = sorted(l, reverse = True)
        res = ''
        k = 0
        for string in l:
            res += string[1] * string[0]
        return res
        