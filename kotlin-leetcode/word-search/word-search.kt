class Solution {
    fun exist(board: Array<CharArray>, word: String): Boolean {
        var index = 0
        board.forEachIndexed{i, row ->
            row.forEachIndexed{j, element ->
                if(dfs(board, i, j, word, index)) return true
            }
        }
        return false
    }
    
    fun dfs(board: Array<CharArray>, i: Int, j: Int, word: String, index: Int): Boolean{
        val row_count = board.count()
        val col_count = board[0].count()
        val word_length = word.length
        val isInvalid = (i<0) || (j<0) || (i>=row_count) || (j>=col_count) || (index>=word_length)
        if(isInvalid) return false
        val targetChar = board[i][j]
        if(targetChar!=word[index]) return false else board[i][j] = '1'
        if(index==word_length-1) return true
        
        val checkLeft = dfs(board, i-1, j, word, index+1)
        val checkRight = dfs(board, i+1, j, word, index+1)
        val checkTop = dfs(board, i, j+1, word, index+1)
        val checkBottom = dfs(board, i, j-1, word, index+1)
        
        
        val hasValidAdjacent = (checkLeft || checkRight || checkTop || checkBottom)
        if(!hasValidAdjacent) board[i][j] = targetChar
         
        return hasValidAdjacent
    }
}