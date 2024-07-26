class Solution {
public:
    int lengthOfLastWord(string s) {
        int len = 0;
        for(int i = s.length() - 1; i >= 0; i--){
            if(len != 0 && s[i] == ' ') return len;
            if(s[i] != ' ') len++;
        }
        return len;
    }
};