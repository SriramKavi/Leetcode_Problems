class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            s = "".join(sorted(list(i)))
            if s in d:
                d[s].append(i)
            else:
                d[s] = [i]
        return list(d.values())