class Solution:
    def divide(self, a: int, b: int) -> int:
        res = 0
        r = 0
        if b < 0:
            b = b * -1
            res = -1
        if a < 0:
            a = a * -1
            r = -1
        ans = a // b
        if (res != - 1 and r == -1) or (res == -1 and r != -1):
            ans = ans * -1
        if ans < -(2 ** 31) :
            return -(2 ** 31)
        elif ans > (2 ** 31) - 1:
            return (2 ** 31) - 1
        else:
            return ans
        
        
        