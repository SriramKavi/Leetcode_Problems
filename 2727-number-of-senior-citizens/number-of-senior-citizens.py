class Solution:
    def countSeniors(self, details: List[str]) -> int:
        cnt = 0
        for d in details:
            k = d[-4] + d[-3]
            if int(k) > 60:
                cnt += 1
        return cnt