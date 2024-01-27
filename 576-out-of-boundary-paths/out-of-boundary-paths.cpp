class Solution {
public:
    long long mod = 1e9 + 7;
    int countPaths(int m, int n, int mM, int i, int j, vector<vector<pair<int, int>>>& dp){
        if(mM < 0) return 0;
        if(i >= m || j >= n || i < 0 || j < 0) return 1;
        if(dp[i][j].first != -1 && dp[i][j].second == mM) return dp[i][j].first;
        int a = countPaths(m, n, mM - 1, i, j + 1, dp) % mod;
        int b = countPaths(m, n, mM - 1, i, j - 1, dp) % mod;
        int c = countPaths(m, n, mM - 1, i + 1, j, dp) % mod;
        int d = countPaths(m, n, mM - 1, i - 1, j, dp) % mod;
        int res = (a % mod + b % mod  + c % mod + d % mod) % mod; 
        dp[i][j] = {res, mM};
        return res;

    }
    int findPaths(int m, int n, int maxMove, int startRow, int startColumn) {
        vector<vector<pair<int, int>>> dp(m, vector<pair<int, int>>(n, {-1, -1}));
        int paths = countPaths(m, n, maxMove, startRow, startColumn, dp);
        return paths;
    }
};