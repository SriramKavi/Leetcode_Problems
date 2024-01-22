class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = []
        for i in nums:
            if i not in l:
                l += [i]
        nums[::] = l[::]
        return len(nums)
                
        