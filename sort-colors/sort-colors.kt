class Solution {
    fun sortColors(nums: IntArray): Unit {
        var endZeroIndex = 0
        var endOneIndex = 0
        var startTwoIndex = nums.count()-1
        
        while(endOneIndex<=startTwoIndex){
            when(nums[endOneIndex]){
               0 -> {
                    val temp = nums[endZeroIndex]
                    nums[endZeroIndex] = 0
                    nums[endOneIndex] = temp
                    endZeroIndex += 1
                    endOneIndex+=1
                }
                1 -> {
                    endOneIndex+=1
                }
                2 -> {
                    val temp = nums[startTwoIndex]
                    nums[startTwoIndex] = 2
                    nums[endOneIndex] = temp
                    startTwoIndex -= 1
                }
            }
        }
    }
}