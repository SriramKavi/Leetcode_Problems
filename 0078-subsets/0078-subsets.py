class Solution:
    def subsets(self, arr: List[int]) -> List[List[int]]:
        n = len(arr)
        l = []
        sub_len = 1 << n
        for i in range(sub_len):
            sub_set = []
            for j in range(32):
                if (i >> j) & 1 > 0:
                    sub_set += [arr[j]]
            l += [sub_set]
        return l