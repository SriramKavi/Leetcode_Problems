class Solution:
    def pathCount(self, i, j, m, n):
        if i >= m or j >= n:
            return 0
        if i == m - 1 and j == n - 1:
            return 1
        if dp[i][j] != -1:
            return dp[i][j]
        dp[i][j] = self.pathCount(i + 1, j, m, n) + self.pathCount(i, j + 1, m, n)
        return dp[i][j]

    def uniquePaths(self, m: int, n: int) -> int:
        global dp
        dp = [[-1] * 101 for _ in range(101)]
        return self.pathCount(0, 0, m, n)