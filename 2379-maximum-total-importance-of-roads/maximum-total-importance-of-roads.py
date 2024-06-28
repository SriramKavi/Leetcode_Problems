class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        arr = [0] * n
        for a, b in roads:
            arr[a] += 1
            arr[b] += 1
        print(arr)
        arr.sort()
        print(arr)
        res = 0
        for i in range(n):
            res += arr[i] * (i + 1)
        return res