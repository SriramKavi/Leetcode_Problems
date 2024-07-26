class Solution:
    def spiralOrder(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])
        l, r, t, b = 0, m - 1, 0, n - 1 
        ans = []
        while l <= r and t <= b:
            for a in range(l, r + 1):
                ans.append(mat[t][a])
            t += 1
            if t > b: break
            for d in range(t, b + 1):
                ans.append(mat[d][r])
            r -= 1
            if r < l: break
            for k in range(r, l - 1, -1):
                ans.append(mat[b][k])
            b -= 1
            if b < t: break
            for p in range(b, t - 1, -1):
                ans.append(mat[p][l])
            l += 1
        return ans