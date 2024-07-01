class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False
        i = 0
        j = 1
        k = 2
        while i < n and j < n and k < n:
            if (arr[i] & 1) and (arr[j] & 1) and (arr[k] & 1):
                return True
            i += 1
            j += 1
            k += 1 
        return False