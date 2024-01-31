class Solution:
    def dailyTemperatures(self, arr: List[int]) -> List[int]:
        res = [0] * (len(arr))
        stack = []
        for i in range(len(arr) - 1, -1, -1):
            while len(stack) != 0 and stack[-1][0] <= arr[i]:
                stack.pop()
            if len(stack) == 0:
                stack.append([arr[i], i])
                res[i] = 0
            else:
                res[i] = stack[-1][1] - i
                stack.append([arr[i], i])
        return res
        