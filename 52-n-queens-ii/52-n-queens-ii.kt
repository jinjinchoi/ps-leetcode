class Solution {
    fun totalNQueens(n: Int): Int {
        val cols = mutableSetOf<Int>()
        val posDiag = mutableSetOf<Int>()
        val negDiag = mutableSetOf<Int>()
        
        var count = 0
        
        fun placeOnRow(row:Int){
            if(row == n){
                count += 1
                return
            }
            for(col in 0..n-1){
                if( col in cols || (row+col) in posDiag || (row-col) in negDiag){
                    continue
                }
                cols.add(col)
                posDiag.add(row+col)
                negDiag.add(row-col)
                
                
                placeOnRow(row+1)
                
                cols.remove(col)
                posDiag.remove(row+col)
                negDiag.remove(row-col)
            }
        }
        
        placeOnRow(0)
    
        return count
        
    }
}