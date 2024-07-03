class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = {}
        for i in magazine:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        cnt = 0
        for i in ransomNote:
            if i in d and d[i] > 0:
                cnt += 1
                d[i] -= 1
        if cnt == len(ransomNote):
            return True
        return False