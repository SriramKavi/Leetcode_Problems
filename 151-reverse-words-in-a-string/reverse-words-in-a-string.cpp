class Solution {
public:
    string reverseWords(string s) {
        vector<string> str;
        string p;
        for(int i = 0; i < s.size(); i++){
            if(s[i] == ' '){
                if(!p.empty()) str.push_back(p);
                p.clear();
            }
            else{
                p += s[i];
            }
        }
        if(!p.empty()) str.push_back(p);
        string res;
        for(int i = str.size() - 1; i >= 0; i--){
            if(i != 0) res += str[i] + " ";
            else res += str[i];
        }
        return res;
    }
};