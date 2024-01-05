class Solution:
    def n2p(self, n):
        c = 0
        i = 0
        while (1 << i) <= n:
            c += 1
            i += 1
        return c - 1

    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return 0
        elif n < 0:
            return False
        if n & (1 << self.n2p(n)) == n:
            return True
        return False
        
