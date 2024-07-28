class Solution {
public:
    int numSq(int n){
        int s = 0;
        while(n){
            s += pow(n % 10, 2);
            n /= 10;
        }
        return s;
    }
    bool isHappy(int n) {
        set<int> st;
        while(true){
            n = numSq(n);
            if(n == 1) return true;
            if(st.find(n) != st.end()) return false;
            st.insert(n);
        }
    }
};