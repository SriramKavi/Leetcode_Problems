class Solution {
public:
    int rangeBitwiseAnd(int left, int right) {
        int low = 0, ind = 0, high = 0;
        for(int i = 31; i >= 0; i--){
            if((left & 1 << i) > 0){
                low = 1 << i;
                ind = i;
                break;
            }
        }
        if(ind == 30){
            high = 2147483647;
        }
        else{
            high = (1 << (ind + 1));
        }
        int res = left;
        if(right <= high){
            for(int j = left; j <= right; j++){
                if(j < 2147483647){
                    res = res & j;
                }
                else{
                    break;
                }
            }
            return res;
        }
        return 0;
    }
};