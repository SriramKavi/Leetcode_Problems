class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        a = []
        b = []
        for i in range(1, n + 1):
            if i % m != 0:
                a += [i]
            else:
                b += [i]
        print(a, b)
        return sum(a) - sum(b)