class Solution {
fun canJump(nums: IntArray): Boolean {
        var answer = false
        val maxIndex = nums.count() - 1
        var lastIndex = maxIndex
        for(i in maxIndex-1 downTo 0){
            if(i+nums[i] >= lastIndex) lastIndex = i
        }
        return lastIndex<=0
    }
}