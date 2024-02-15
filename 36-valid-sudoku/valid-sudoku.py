class Solution:
    def check(self, arr):
            c = 0
            p = []
            for i in arr:
                if i not in p or i == '.':
                    p += [i]
            return len(p) == 9

    def isValidSudoku(self, arr: List[List[str]]) -> bool:
        r = 9
        c = 9
        for i in range(r):
            rflag = False
            cflag = False
            l = []
            k = []
            for j in range(c):
                if arr[j][i] not in k or arr[j][i] == ".":
                    k += [arr[j][i]]
                    cflag = True
                if arr[i][j] not in l or arr[i][j] == ".":
                    l += [arr[i][j]]
                    rflag = True
            if len(l) != 9:
                rflag = False
                break
            if len(k) != 9:
                cflag = False
                break
        mat3 = []
        for i in range(0, r, 3):
            for j in range(0, c, 3):
                mat3.append(arr[i][j:j + 3] + arr[i + 1][j:j + 3] + arr[i + 2][j:j + 3])
        tf = True
        for i in mat3:
            if not self.check(i):
                tf = False
                break
        return tf and rflag and cflag