class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        s = "".join(chars)
        c = 1
        l = []
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                c += 1
            else:
                l.append(s[i])
                if c != 1 and c < 10:
                    l.append(str(c))
                elif c >= 10:
                    l += list(str(c))
                c = 1
        l.append(s[-1])
        if c != 1 and c < 10:
            l.append(str(c))
        elif c >= 10:
            l += list(str(c))
        chars[::] = l[::]
        return len(chars)
