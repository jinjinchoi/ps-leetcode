def knap_sack(profits, profits_length, weights, capacity):
    def dfs(profits, profits_length, weights, capacity, index):
        if index >= profits_length:
            return 0
        
        profit_1 = 0
        if weights[index] <= capacity:
            profit_1 = profits[index] + dfs(profits, profits_length, weights, capacity-weights[index], index+1)
        profit_2 = dfs(profits, profits_length, weights, capacity, index+1)
        return max(profit_1, profit_2)
    
    return dfs(profits, profits_length, weights, capacity, 0)

profits = [60, 100, 120] 
profits_length = 3
weights = [10, 20, 30] 
capacity = 50 
print(knap_sack(profits, profits_length, weights, capacity))
