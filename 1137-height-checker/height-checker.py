class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        s = heights.copy()
        n = len(heights)
        s.sort()
        c = 0
        for i in range(n):
            if heights[i] != s[i]:
                c += 1
        return c