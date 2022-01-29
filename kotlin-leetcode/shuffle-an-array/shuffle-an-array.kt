class Solution(nums: IntArray) {
    val initial = nums.copyOf()
    var shuffled = nums
    val random = Random()

    fun reset(): IntArray {
        return initial
    }

    fun shuffle(): IntArray {
        for(i in 0..initial.size-1){
            swap(shuffled, i, random.nextInt(shuffled.size))
        }
        return shuffled
    }
    
    fun swap(nums:IntArray, i:Int, j:Int){
        val temp = nums[j]
        nums[j] = nums[i]
        nums[i] = temp
    }

}

/**
 * Your Solution object will be instantiated and called as such:
 * var obj = Solution(nums)
 * var param_1 = obj.reset()
 * var param_2 = obj.shuffle()
 */