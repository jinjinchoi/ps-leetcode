class Solution {
public:
    char findTheDifference(string s, string t) {
        unordered_map<char, int> s_map;
        for(auto& c: s){
            s_map[c] += 1;
        }
        for(auto& c: t){
            s_map[c] -= 1;
            if(s_map[c] < 0){
                return c;
            }
        }
        return '\0';
    }
};