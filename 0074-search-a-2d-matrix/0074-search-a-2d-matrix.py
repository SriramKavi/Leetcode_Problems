class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flag = False
        for arr in matrix:
            l = 0
            h = len(arr) - 1
            while l <= h:
                mid = (l + h) // 2
                if arr[mid] == target:
                    flag = True
                    return True
                elif arr[mid] > target:
                    h = mid - 1
                else:
                    l = mid + 1
        return flag
                
            