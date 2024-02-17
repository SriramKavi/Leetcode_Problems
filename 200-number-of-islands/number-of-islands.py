class Solution:
    def nIslands(self, i, j, grid, m, n, vis):
        if i >= m or j >= n or i < 0 or j < 0 or grid[i][j] == '0' or vis[i][j] == '1':
            return
        vis[i][j] = '1'
        self.nIslands(i, j + 1, grid, m, n, vis)
        self.nIslands(i + 1, j, grid, m, n, vis)
        self.nIslands(i - 1, j, grid, m, n, vis)
        self.nIslands(i, j - 1, grid, m, n, vis)

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        vis = [['0'] * (n) for _ in range(m)]
        cnt  = 0
        for i in range(m):
            for j in range(n):
                if vis[i][j] == '0' and grid[i][j] == '1':
                    cnt += 1
                    self.nIslands(i, j, grid, m, n, vis)
        return cnt