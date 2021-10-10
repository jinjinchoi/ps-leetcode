class Solution {
    fun rangeBitwiseAnd(left: Int, right: Int): Int {
        // finding common prefix of left & right
        var shift = 0
        var from = left
        var to = right
        
        while(from != to){
            from = from shr 1
            to = to shr 1
            shift += 1
        }
        
        return from shl shift
    }
}