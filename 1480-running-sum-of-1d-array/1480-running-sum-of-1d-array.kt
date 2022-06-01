class Solution {
    fun runningSum(nums: IntArray): IntArray {
        val result = IntArray(nums.size)
        result[0] = nums[0]
        nums.drop(1).forEachIndexed{ i, num ->
            result[i+1] = num + result[i]
        }
        return result
    }
}