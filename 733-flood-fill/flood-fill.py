class Solution:
    def floodfill(self, i, j, image, color, m, n, vis, d):
        if i >= m or j >= n or i < 0 or j < 0 or vis[i][j] == 1 or image[i][j] != d:
            return
        vis[i][j] = 1
        image[i][j] = color
        self.floodfill(i + 1, j, image, color, m, n, vis, d)
        self.floodfill(i, j + 1, image, color, m, n, vis, d)
        self.floodfill(i- 1, j, image, color, m, n, vis, d)
        self.floodfill(i, j - 1, image, color, m, n, vis, d)



    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        vis = [[0] * (n) for _ in range(m)]
        d = image[sr][sc]
        self.floodfill(sr, sc, image, color, m, n, vis, d)
        return image