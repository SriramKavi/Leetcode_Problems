class Solution:
    def power(self, a, b):
        mod = 1337
        res = 1
        while b:
            if (b & 1):
                b = b - 1
                res = ((res % mod) * (a % mod)) % mod
            else:
                b = b // 2
                a = ((a % mod) * (a % mod)) % mod
        return res
        
    def superPow(self, a: int, b: List[int]) -> int:
        b = int("".join(list(map(str, b))))
        ans = self.power(a, b)
        return ans
        
        