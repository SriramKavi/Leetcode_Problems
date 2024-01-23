class Solution:
    def checkUnique(self, s: str) -> bool:
        a = set(s)
        if len(a) == len(s):
            return True
        return False
    
    def maxLength(self, arr: List[str]) -> int:
        n = len(arr)
        l = []
        sub_len = 1 << n
        for i in range(sub_len):
            res = ''
            for j in range(32):
                if (i >> j) & 1 > 0:
                    res += arr[j]
            if self.checkUnique(res):
                l += [len(res)]
        return max(l)