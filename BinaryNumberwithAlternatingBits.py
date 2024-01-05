class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        if n == 1:
            return 1
        if (n & 1) == 1:
            flag = 0
        else:
            flag = 1
        while n:
            if flag == (n & 1):
                return 0
            else:
                flag = (n & 1)
                n = n >> 1
        return 1
        
