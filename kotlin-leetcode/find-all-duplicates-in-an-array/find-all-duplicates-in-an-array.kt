class Solution {
    fun findDuplicates(nums: IntArray): List<Int> {
        var twice = arrayListOf<Int>()
        nums.forEachIndexed{i, num ->
            val idx = Math.abs(num)-1
            if(nums[idx]<0) twice.add(idx+1)
            nums[idx] *= -1
        }
        return twice.toList()
    }
}