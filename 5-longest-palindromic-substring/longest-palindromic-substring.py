class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = []
        m = 1
        nw = ""
        for i in range(n):
            for j in range(i, n):
                k = s[i:j + 1]
                if k == k[::-1]:
                    if len(k)>=m:
                        m = len(k)
                        nw = k 
        return nw            

        # return ""