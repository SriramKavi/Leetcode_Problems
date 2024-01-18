class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        res = 0
        od = 0
        for i in list(d.values()):
            if i % 2 == 0:
                res += i
            elif i % 2 != 0 and od == 0:
                res += i
                od+=1
            else:
                res += (i//2) * 2
        return res
                
        
        
                                                                                             