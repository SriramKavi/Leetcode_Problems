class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        l = [i for i in range(1, len(nums) + 1)]
        rep = 0
        mis = 0
        for i in range(len(l)):
            if l[i] not in nums:
                mis = l[i]
                break
        for i in range(len(nums)):
            if nums.count(nums[i]) > 1:
                rep = nums[i]
                break
        return [rep, mis]
        