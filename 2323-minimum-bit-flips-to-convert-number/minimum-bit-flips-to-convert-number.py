import math
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        c = 0
        res = start ^ goal
        while res:
            if res & 1 == 1:
                c += 1
            res = res >> 1
        return c
        
            