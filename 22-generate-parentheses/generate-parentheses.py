class Solution:
    def generatePar(self, op, cl, n, st, ans):
        if op == n and cl == n:
            ans.append(st)
            return
        if op < n:
            self.generatePar(op + 1, cl, n, st + '(', ans)
        if cl < op:
            self.generatePar(op, cl + 1, n, st + ')', ans)


    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.generatePar(0, 0, n, '', ans)
        return ans