class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        d = {}
        for i in range(n):
            d[heights[i]] = names[i]
        l = list(d.keys())
        l = sorted(l, reverse = True)
        ans = []
        for i in l:
            ans.append(d[i])
        return ans