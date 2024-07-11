class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        stack = []
        p = []
        for i in range(n):
            if s[i] != ')':
                stack.append(s[i])
            else:
                while len(stack) and stack[-1] != '(':
                    p.append(stack.pop())
                if len(stack): stack.pop()
                stack.extend(p)
                p = []
        return "".join(stack)

            

            