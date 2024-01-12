class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        first_half = s[0:n // 2]
        second_half = s[n // 2:]
        vowels = 'aeiouAEIOU'
        c1 = 0
        c2 = 0
        for i in first_half:
            if i in vowels:
                c1 += 1
        for i in second_half:
            if i in vowels:
                c2 += 1
        return c1 == c2