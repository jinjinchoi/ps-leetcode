class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int m = word1.size();
        int n = word2.size();
        string output = "";
        int i = 0, j = 0;
        
        while(i<m || j<n){
            if(i<m){
                output.push_back(word1[i++]);
            }
            if(j<n){
                output.push_back(word2[j++]);
            }
        }
        return output;
    }
};