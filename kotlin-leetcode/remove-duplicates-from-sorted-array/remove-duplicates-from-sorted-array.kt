class Solution {
    fun removeDuplicates(nums: IntArray): Int {
        var uniqueMaxIndex = 0
        var targetIndex = 1
        
        while(targetIndex < nums.size){
            if(nums[uniqueMaxIndex] == nums[targetIndex]){
                targetIndex += 1
            }else{
                for(i in uniqueMaxIndex+1..targetIndex-1){
                    nums[i] = nums[targetIndex]
                }
                targetIndex += 1
                uniqueMaxIndex += 1
            }
        }
        
        return uniqueMaxIndex+1 
    }
}