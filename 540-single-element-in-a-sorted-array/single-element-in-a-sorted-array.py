class Solution:
    def singleNonDuplicate(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return arr[0]
        l = 0
        h = n - 1
        while l <= h:
            mid = (l + h) // 2
            if mid % 2 == 0:
                if mid < n - 1 and arr[mid] == arr[mid + 1]:
                    l = mid + 1
                else:
                    h = mid - 1
            else:
                if mid > 0 and (arr[mid] == arr[mid - 1]):
                    l = mid + 1
                else:
                    h = mid - 1
        return arr[l]
                
        
        
            
            