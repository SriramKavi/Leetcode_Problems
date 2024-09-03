class Solution {
public:
    int getLucky(string s, int k) {
        string str;
        int i = 0;
        while(i < s.size()){
            str += to_string(int(s[i]) - 96);
            i++;
        }
        int res = 0;
        while(k--){
            for(auto it: str){
                res += int(it) - '0';
            }
            str = to_string(res);
            res = 0;
        }
        return stoi(str);
    }
};