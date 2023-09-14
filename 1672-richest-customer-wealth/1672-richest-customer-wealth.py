class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        curr_wealth = 0
        for customer_account in accounts:
            for a in customer_account:
                curr_wealth += a
            if(curr_wealth > max_wealth):
                max_wealth = curr_wealth
            curr_wealth = 0
        return max_wealth