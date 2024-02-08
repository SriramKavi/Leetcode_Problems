class Solution:
    def perfectsq(self, n):
        if n == 0:
            return 0
        ans = (10 ** 5) + 1
        if dp[n] != -1:
            return dp[n]
        for i in range(1, int(n ** 0.5) + 1):
            if i * i <= n:
                ans = min(ans, self.perfectsq(n - (i * i)) + 1)
        dp[n] = ans
        return dp[n]

    def numSquares(self, n: int) -> int:
        global dp
        dp = [-1] * (n + 1)
        return self.perfectsq(n)