class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        res = []
        nums.sort()
        c = 0
        for i in range(0, len(nums), 3):
            res.append(nums[i:3 + i])
        for arr in res:
            if abs(arr[0] - arr[-1]) <= k:
                c += 1
        if c == (len(nums) // 3):
            return res
        return []
        