class Solution {
public:
    bool isPalindrome(string s) {
        string str;
        for(auto st: s){
            if(isalnum(st)){
                str += tolower(st);
            }
        }
        string res;
        for(int i = str.size() - 1; i >= 0; i--){
            res += str[i];
        }
        return (str == res);
    }
};