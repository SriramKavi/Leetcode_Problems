class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        s = 0
        temp = x
        while x:
            r = x % 10
            s = s * 10 + r
            x = x // 10
        return s == temp