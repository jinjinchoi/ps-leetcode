class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        int maxWealth = 0;
        for(vector<int>& account : accounts){
            int currWealth = 0;
            for(int money: account){
                currWealth += money;
            }
            maxWealth = max(maxWealth, currWealth);
        }
        return maxWealth;
    }
};