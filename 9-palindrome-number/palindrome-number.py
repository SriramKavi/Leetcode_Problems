class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        x1 = x[-1::-1]
        if x1 == x:
            return True
        else:
            return False