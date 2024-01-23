class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        j = len(nums) - 1
        l = []
        while i < j:
            l += [nums[i] + nums[j]]
            i += 1
            j -= 1
        return max(l)