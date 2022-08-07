class Solution {
    fun solution(numbers: IntArray): IntArray {
        var answer: IntArray = intArrayOf()
        numbers.sort()
        val numSet = mutableSetOf<Int>()

        for(i in 0 until numbers.size){
            for(j in i+1 until numbers.size){
                numSet.add(numbers[i] + numbers[j])
            }
        }

        return numSet.sorted().toIntArray()
    }
}
