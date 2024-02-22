class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        r = len(matrix)
        res = []
        for i in range(r):
            l = []
            for j in range(r):
                l.append(matrix[j][i])
            l.reverse()
            res.append(l)
        matrix[::] = res
        