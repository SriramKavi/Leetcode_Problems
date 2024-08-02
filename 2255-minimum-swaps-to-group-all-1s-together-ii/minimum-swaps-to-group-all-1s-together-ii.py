class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ones = sum(nums)
        nums = nums + nums[:ones - 1]
        n = len(nums)
        for i in range(1, n):
            nums[i] += nums[i - 1]
        st, end = 1, ones
        m = ones - nums[end - 1]
        while st < n and end < n:
            m = min(m, ones - (nums[end] - nums[st - 1]))
            st += 1
            end += 1
        return m
