class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        vis = [[0] * (n) for _ in range(m)]
        t = 0
        q = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append([i, j, t])
                    vis[i][j] = 2
        drow = [-1, 0, 1, 0]
        dcol = [0, 1, 0, -1]
        while len(q) != 0:
            r = q[0][0]
            c = q[0][1]
            t = q[0][2]
            q.pop(0)
            for x in range(4):
                i = r + drow[x]
                j = c + dcol[x]
                if i >= 0 and i < m and j >= 0 and j < n and vis[i][j] != 2 and grid[i][j] == 1:
                    q.append([i, j, t + 1])
                    vis[i][j] = 2
        for i in range(m):
            for j in range(n):
                if vis[i][j] != 2 and grid[i][j] == 1:
                    return -1
        return t
