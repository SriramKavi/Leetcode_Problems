class Solution:
    def combination_Sum(self, ind, arr, n, k, ds, res):
        if ind == n:
            if k == 0:
                a = ds.copy()
                res.append(a)
            return
        if arr[ind] <= k:
            ds.append(arr[ind])
            k = k - arr[ind]
            self.combination_Sum(ind, arr, n, k, ds, res)
            k = k + arr[ind]
            ds.pop()
        self.combination_Sum(ind + 1, arr, n, k, ds, res)
        return res

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ds = []
        res = []
        self.combination_Sum(0, candidates, len(candidates), target, ds, res)
        return res
        