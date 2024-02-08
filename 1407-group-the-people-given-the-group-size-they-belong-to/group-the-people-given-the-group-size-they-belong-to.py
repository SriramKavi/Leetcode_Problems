class Solution:
    def groupThePeople(self, arr: List[int]) -> List[List[int]]:
        d = {}
        l = []
        for i in range(len(arr)):
            if arr[i] in d and len(d[arr[i]]) == arr[i]:
                l.append(d[arr[i]])
                d[arr[i]] = [i]
            elif arr[i] in d and len(d[arr[i]]) <= arr[i]:
                d[arr[i]].append(i)
            else:
                d[arr[i]] = [i]
        for k, v in d.items():
            l.append(v)
        return l
        
