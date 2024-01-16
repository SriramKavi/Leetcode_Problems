class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 2:
            return 1
        return self.fib(n - 1) + self.fib(n - 2)
        # a = 0
        # b = 1
        # l = [a, b]
        # while n > 1:
        #     n -= 1
        #     c = a + b
        #     l += [c]
        #     a = b
        #     b = c
        # return l[-1]