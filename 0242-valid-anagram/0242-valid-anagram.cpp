class Solution {
public:
    bool isAnagram(string s, string t) {
        int len_s = s.length();
        int len_t = t.length();
        if(len_s != len_t){
            return false;
        }
        unordered_map<char, int> counter;
        for(int i=0; i<len_s; i++){
            counter[s[i]] += 1;
            counter[t[i]] -= 1;
        }
        for(auto count: counter){
            if(count.second){
                return false;
            }
        }
        return true;
    }
};