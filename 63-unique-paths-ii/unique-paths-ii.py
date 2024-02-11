class Solution:
    def countPaths(self, i, j, m, n, grid):
        if i >= m or j >= n or grid[i][j] == 1:
            return 0
        if i == m - 1 and j == n - 1:
            return 1
        if dp[i][j] != -1:
            return dp[i][j]
        dp[i][j] = self.countPaths(i + 1, j, m, n, grid) + self.countPaths(i, j + 1, m, n, grid)
        return dp[i][j]

    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        global dp
        dp = [[-1] * 101 for _ in range(101)]
        return self.countPaths(0, 0, m, n, grid)