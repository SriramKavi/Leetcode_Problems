class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        for i in nums:
            if i < 0:
                neg += [i]
            else:
                pos += [i]
        new = []
        i = 0
        j = 0
        while i < len(pos) and j < len(neg):
            new += [pos[i], neg[i]]
            i += 1
            j += 1
        return new