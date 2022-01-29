class Solution {
    fun rotate(nums: IntArray, k: Int): Unit {
        var minMove = k.rem(nums.size)
        var temporary = nums.sliceArray(nums.size-minMove..nums.size-1)

        for(i in 0..nums.size-minMove-1){
            nums[nums.size -1 - i] = nums[nums.size-minMove-1-i]
        }
        for(i in 0.. minMove-1){
            nums[i] = temporary[i]
        }
    }
}