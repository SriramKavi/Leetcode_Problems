class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        tot = (n * (n + 1)) // 2
        s = sum(nums)
        return tot - s