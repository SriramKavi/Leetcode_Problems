class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def map(n):
            s = 0
            i = 0
            if n == 0:
                return mapping[n]
            while n:
                r = n % 10
                r = mapping[r]
                s += r * pow(10, i)
                i += 1
                n //= 10
            return s 
        ans = sorted(nums, key = lambda p: map(p))
        return ans