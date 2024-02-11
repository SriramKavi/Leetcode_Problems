class Solution:
    def generateSubsets(self, ind, n, nums, ds, ans):
        if ind == n:
            d = ds.copy()
            ans.append(ds)
            return
        self.generateSubsets(ind + 1, n, nums, ds + [nums[ind]], ans)
        self.generateSubsets(ind + 1, n, nums, ds, ans)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ds = []
        ans = []
        self.generateSubsets(0, n, nums, ds, ans)
        return ans