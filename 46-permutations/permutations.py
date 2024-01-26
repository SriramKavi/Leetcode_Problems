class Solution:
    def printPermutations(self, s, frq, ans, res):
        if len(ans) == len(s):
            a = ans.copy()
            res += [a]
            return
        for i in range(0, len(s)):
            if frq[i] == 0:
                frq[i] = 1
                self.printPermutations(s, frq, ans + [s[i]], res)
                frq[i] = 0
        return res

    def permute(self, nums: List[int]) -> List[List[int]]:
        frq = [0] * len(nums)
        res = []
        self.printPermutations(nums, frq, [], res)
        return res