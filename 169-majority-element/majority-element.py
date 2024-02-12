class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums) // 2
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for a, b in d.items():
            if b > n:
                return a
        return -1