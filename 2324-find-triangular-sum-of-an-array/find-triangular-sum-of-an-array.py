class Solution:
    def triSum(self, nums):
        newNums = []
        for i in range(len(nums) - 1):
            newNums.append((nums[i] + nums[i + 1]) % 10)
        nums[::] = newNums[::]
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) > 1:
            self.triSum(nums)
        return nums[0]


