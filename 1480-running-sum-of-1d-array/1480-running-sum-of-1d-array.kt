class Solution {
    fun runningSum(nums: IntArray): IntArray {
        nums.drop(1).forEachIndexed{ i, num ->
            nums[i+1] = num + nums[i]
        }
        return nums
    }
}