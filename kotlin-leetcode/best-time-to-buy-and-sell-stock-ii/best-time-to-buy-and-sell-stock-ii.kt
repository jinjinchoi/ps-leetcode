class Solution {
    fun maxProfit(prices: IntArray): Int {
	var min_index = 0
    var max_index = 0
    var profit_sum = 0
    
    while(max_index < prices.size-1){
        if(prices[max_index+1]<prices[max_index]){
            profit_sum += (prices[max_index]-prices[min_index])
            min_index = max_index+1
            max_index = min_index
        }else{
            max_index += 1
        }
    }
    if(max_index == prices.size-1)
    	profit_sum += (prices[prices.size-1]-prices[min_index])
    return profit_sum
}
}