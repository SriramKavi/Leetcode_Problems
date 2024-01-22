class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int s = 0, m = 0;
        int n = nums.size();
        for(int i = 0; i < n; i++){
            s += nums[i];
            if(s < 0) s = 0;
            if(s > m) m = max(m, s);
        }
        if(m == 0){
            auto it = *max_element(nums.begin(),nums.end());
            return it;
        }
        return m;
    }
};