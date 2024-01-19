class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        neg = []
        pos = []
        for i in nums:
            if i < 0:
                neg += [i]
            else:
                pos += [i]
        res = []
        for i in range(len(neg)):
            res += [pos[i], neg[i]]
        return res