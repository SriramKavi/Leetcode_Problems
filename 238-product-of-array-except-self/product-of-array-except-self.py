class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pf = [1] * n
        for i in range(1, n):
            pf[i] =  pf[i - 1] * nums[i - 1]
        sf = [1] * n
        for i in range(n - 2, -1, -1):
            sf[i] = sf[i + 1] * nums[i + 1]
        res = []
        for i in range(n):
            res.append(pf[i] * sf[i])
        return res