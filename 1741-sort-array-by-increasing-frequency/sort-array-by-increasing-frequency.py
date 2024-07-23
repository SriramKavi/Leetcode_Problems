class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d = {}
        for i in nums:
            if i not in d: d[i] = 1
            else: d[i] += 1
        x = lambda p: (-d[p], p)
        ans = sorted(nums, key = x, reverse = True)
        return ans