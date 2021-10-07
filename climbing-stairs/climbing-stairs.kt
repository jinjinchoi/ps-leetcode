class Solution {
    fun climbStairs(n: Int): Int {
        var numArray = IntArray(n)
        if(n==1) return 1
        if(n==2) return 2
        numArray[0] = 1
        numArray[1] = 2
        for(i in 2..n-1){
            numArray[i] = numArray[i-1] + numArray[i-2]
        }
        return numArray[n-1]
    }
}