class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ind = 0
        cnt = 0
        while ind < len(nums):
            i = ind
            j = i + 1
            while j < len(nums):
                if nums[i] == nums[j] and i < j:
                    cnt += 1
                j += 1
            ind += 1
        return cnt
                