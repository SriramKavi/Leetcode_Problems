class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        d = {}
        for i in target:
            if i not in d: d[i] = 1
            else: d[i] += 1
        for i in arr:
            if i in d:
                d[i] -= 1
                if d[i] < 0:
                    return False
            else:
                return False
        return True