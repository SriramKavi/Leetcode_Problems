class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        h = n - 1
        res = 0
        mxL = 0
        mxR = 0
        while l <= h:
            if height[l] <= height[h]:
                if height[l] >= mxL:
                    mxL = height[l]
                else:
                    res += mxL - height[l]
                l += 1
            else:
                if height[h] >= mxR:
                    mxR = height[h]
                else:
                    res += mxR - height[h]
                h -= 1
        return res
                        