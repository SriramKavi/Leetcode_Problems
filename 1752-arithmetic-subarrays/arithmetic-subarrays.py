class Solution:
    def isArt(self, arr):
        if len(arr) < 2:
            return False
        arr = sorted(arr, reverse = True)
        diff = arr[1] - arr[0]
        for i in range(1, len(arr) - 1):
            if arr[i + 1] - arr[i] != diff:
                return False
        return True

    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        n = len(l)
        res = []
        for i in range(n):
            if self.isArt(nums[l[i]:r[i] + 1]):
                res.append(True)
            else:
                res.append(False)
        return res