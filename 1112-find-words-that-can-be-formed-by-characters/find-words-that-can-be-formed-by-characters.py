class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        d = {}
        for i in chars:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        ans = 0
        for i in words:
            s = ''
            c = dict(d)
            print(c)
            for j in i:
                if j in c and c[j] > 0:
                    s += j
                    c[j] -= 1
            if s == i:
                ans += len(i)
        return ans
