class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        m = -1
        while i <= j:
            d = j - i
            a = d * min(height[i], height[j])
            if a > m:
                m = a
            if height[i] < height[j]:
                i += 1
            elif height[j] < height[i]:
                j -= 1
            else:
                i += 1
                j -= 1
        return m