class Solution:
    def binaryB(self, n, base):
        s = ""
        while n:
            s += str(n % base)
            n = n // base
        return s[::-1]


    def isStrictlyPalindromic(self, n: int) -> bool:
        base = 2
        while base <= n - 2:
            ans = self.binaryB(n, base)
            base += 1
            if ans != ans[::-1]:
                return False
        return True