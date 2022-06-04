class Solution {
    fun solveNQueens(n: Int): List<List<String>> {
        val cols = mutableSetOf<Int>()
        val posDiag = mutableSetOf<Int>()
        val negDiag = mutableSetOf<Int>()
        
        val result = mutableListOf<List<String>>()
        val board = MutableList(n) {  MutableList(n){ "." } }

        
        fun placeOnRow(row:Int){
            if(row == n){
                val temp = mutableListOf<String>()
                board.forEach{ row ->
                   temp.add(row.joinToString(""))
                }
                result.add(temp)
                return
            }
            for(col in 0..n-1){
                if( col in cols || (row+col) in posDiag || (row-col) in negDiag){
                    continue
                }
                cols.add(col)
                posDiag.add(row+col)
                negDiag.add(row-col)
                board[row][col] = "Q"
                
                placeOnRow(row+1)
                
                cols.remove(col)
                posDiag.remove(row+col)
                negDiag.remove(row-col)
                board[row][col] = "."
            }
        }
        
        placeOnRow(0)
    
        return result
        
    }
    
    
    
}