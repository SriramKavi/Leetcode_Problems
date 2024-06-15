class Solution:
    def fun(self, s, idx, rewardValues, n):
        if idx == n:
            return s
        if s > rewardValues[-1]:
            return s
        if dp[idx][s] != 0:
            return dp[idx][s]
        pick = 0
        nonpick = 0
        if rewardValues[idx] > s:
            pick = self.fun(s + rewardValues[idx], idx + 1, rewardValues, n)
        else:
            pick = self.fun(s, idx + 1, rewardValues, n)
        nonpick = self.fun(s, idx + 1, rewardValues, n)
        dp[idx][s] = max(pick, nonpick)
        return dp[idx][s]


    def maxTotalReward(self, rewardValues: List[int]) -> int:
        global dp
        dp = [[0] * 2001] * 4001
        n = len(rewardValues)
        rewardValues.sort()
        return self.fun(0, 0, rewardValues, n)
