class Solution {
public:
    long long maximumImportance(int n, vector<vector<int>>& roads) {
        vector<long long> arr(n,0);
        for(auto it : roads){
            arr[it[0]]++;
            arr[it[1]]++;
        }
        sort(arr.begin(), arr.end());
        long long s = 0;
        for(int i = 0; i < n; i++){
            s += arr[i] * (i + 1);
        }
        return s;
    }
};