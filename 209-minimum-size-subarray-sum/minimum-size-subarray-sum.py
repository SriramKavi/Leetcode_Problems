class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, s = 0, 0
        n = len(nums)
        m = float('inf')
        for r in range(n):
            s += nums[r]
            while s >= target:
                m = min(m, r - l + 1)
                s -= nums[l]
                l += 1
            r += 1
        return 0 if m == float('inf') else m