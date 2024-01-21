class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0:
            return 0
        if len(s) != 1 and (s[1] == '+' or s[1] == '-') and s[0].isdigit() == False:
            return 0
        if s[0] == '-':
            res = ''
            for i in range(1, len(s)):
                if s[i].isdigit():
                    res += s[i]
                elif s[i].isdigit() == False:
                    break
            if res == '':
                return 0
            if (int(res) * -1) <= (-2 ** 31):
                return (-2 ** 31)
            return int(res) * -1
        else:
            if s[0].isdigit():
                res = s[0]
            else:
                res = ''
            if s[0].isdigit() == False and s[0] != '+':
                return 0
            for i in range(1, len(s)):
                if s[i].isdigit():
                    res += s[i]
                elif s[i].isdigit() == False:
                    break
            if res == '':
                return 0
            if int(res) >= (2 ** 31 - 1):
                return (2 ** 31 - 1)
            return int(res)
