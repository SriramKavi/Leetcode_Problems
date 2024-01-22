from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res_perm = permutations(nums)
        l = []
        for i in list(res_perm):
            l += [i]
        return l
        