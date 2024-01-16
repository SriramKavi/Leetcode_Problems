class Solution:
    def group_Anagrams(self, strs) -> List[List[str]]:
        d = {}
        for i in strs:
            s = "".join(sorted(i))
            if s in d:
                d[s] += [i]
            else:
                d[s] = [i]
        return d.values()
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans =  self.group_Anagrams(strs)
        return ans