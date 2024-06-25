class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = []
        for i in nums:
            if i != val:
                l += [i]
        nums[::] = l[::]
        return len(nums)