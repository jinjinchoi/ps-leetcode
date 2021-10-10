class Solution {
    fun rangeBitwiseAnd(left: Int, right: Int): Int {
        // finding common prefix of left & right
        var shift = 1
        var from = left
        var to = right
        
        while(from != to){
            from = from shr 1
            to = to shr 1
            shift = shift shl 1
        }
        
        return shift * from
    }
}