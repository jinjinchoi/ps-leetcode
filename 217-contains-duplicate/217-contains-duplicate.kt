class Solution {
    fun containsDuplicate(nums: IntArray): Boolean {
        val indexHash: HashSet<Int> = HashSet()
        nums.forEach{ num ->
            if(indexHash.contains(num)) return true
            indexHash.add(num)
        }
        return false
    }
}