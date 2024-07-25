class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxi = 0
        while l <= r:
            m = min(height[l], height[r])
            ans = m * (r - l)
            maxi = max(ans, maxi)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxi