class Solution {
public:
    bool isAnagram(string s, string t) {
        int len_s = s.length();
        int len_t = t.length();
        if(len_s != len_t){
            return false;
        }
        int count_array[26] = {0};
        for(int i=0; i<len_s; i++){
            count_array[s[i]-'a'] += 1;
            count_array[t[i]-'a'] -= 1;
        }
        for(int i=0; i<26; i++){
            if(count_array[i]){
                return false;
            }
        }
        return true;
    }
};