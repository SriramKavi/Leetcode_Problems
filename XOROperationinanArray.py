class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        i = 0
        nums = []
        while i < n:
            nums += [start + 2 * i]
            i += 1
        res = nums[0]
        for i in range(1, len(nums)):
            res = res ^ nums[i]
        return res
