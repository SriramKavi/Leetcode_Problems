class Solution:
    def map(self, n, mapping):
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


    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapped = []
        for i in range(len(nums)):
            mapped.append((self.map(nums[i], mapping), i))
        x = lambda a: (a[0], a[1])
        ans = sorted(mapped, key = x)
        res = []
        for k, v in ans:
            res.append(nums[v])
        return res
