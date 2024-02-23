class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        d = {}
        for _id, time in logs:
            if _id in d:
                if time not in d[_id]:
                    d[_id].append(time)
            else:
                d[_id] = [time]
        l = list(d.values())
        l = list(map(len, l))
        d1 = {}
        for i in l:
            if i in d1:
                d1[i] += 1
            else:
                d1[i] = 1
        print(d1)
        res = [0] * k
        for i, j in d1.items():
            res[i - 1] = j
        return res