class Solution {
    fun search(nums: IntArray, target: Int): Int {
        nums.forEachIndexed{ i, num ->
            if(target==num) return@search i
        }
        return -1
    }
}