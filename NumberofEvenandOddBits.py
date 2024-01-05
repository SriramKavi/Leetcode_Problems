class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        e = 0
        od = 0
        l = []
        i = 0
        while n:
            if n & 1 == 1 and i % 2 == 0:
                e += 1
            elif n & 1 == 1 and i % 2 != 0:
                od += 1
            i += 1
            n = n >> 1
        l += [e, od]
        return l
        
