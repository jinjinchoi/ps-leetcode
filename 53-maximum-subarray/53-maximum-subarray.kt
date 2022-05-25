class Solution {
    fun maxSubArray(nums: IntArray): Int {
        var partialSum = 0
        var maxSum = nums[0]
        
        nums.forEach{ num ->
            partialSum += num
            maxSum = if (partialSum > maxSum) partialSum else maxSum
            if(partialSum < 0){
                partialSum = 0
                return@forEach
            }
            // maxSum = if (partialSum > maxSum) partialSum else maxSum
        }  
        return maxSum
    }
}