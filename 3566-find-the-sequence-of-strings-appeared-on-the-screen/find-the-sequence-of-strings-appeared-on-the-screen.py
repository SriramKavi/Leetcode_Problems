class Solution:
    def stringSequence(self, target: str) -> List[str]:
        ptr = 0
        n = len(target)
        s = "a"
        res = [s]
        while target != res[-1]:
            if target[ptr] != res[-1][-1]:
                k = res[-1]
                if len(k) != 1:
                    if res[-1][-1] == 'z':
                        res.append(res[-1][:-1] + 'a')
                    else:
                        p = chr(ord(res[-1][-1]) + 1)
                        res.append(res[-1][:-1] + p)
                else:
                    if k == 'z': res.append('a')
                    else: res.append(chr(ord(k) + 1))
            else:
                res.append(res[-1])
                res[-1] += 'a'
                ptr += 1
        return res
                
                