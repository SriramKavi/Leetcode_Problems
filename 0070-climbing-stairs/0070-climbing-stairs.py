class Solution:
    def climbStairs(self, n: int) -> int:
        a = 0
        b = 1
        i = 0
        while i < n:
            c = a + b
            a = b
            b = c
            i += 1
        return c
        