class Solution {
    fun reverseString(s: CharArray): Unit {
        for(i in 0..s.size/2-1){
            var temp = s[i]
            s[i] = s[s.size-1-i]
            s[s.size-1-i] = temp
        }
    }
}