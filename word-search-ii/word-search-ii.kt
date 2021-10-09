class Solution {
    fun findWords(board: Array<CharArray>, words: Array<String>): List<String> {
        var output = arrayListOf<String>()
        words.forEach word@{ word ->
            board.forEachIndexed{ i, row -> 
                row.forEachIndexed{ j, element ->
                    if(dfs(board, i, j, word, 0)){
                        output.add(word)
                        return@word
                    }
                }
            }
            
        }
        return output
    }
    
    fun dfs(board: Array<CharArray>, row: Int, col: Int, word: String, index: Int): Boolean{
        val m = board.count()
        val n = board[0].count()
        val isOutOfArrayBounds = (row<0) || (col<0) || (row>=m) || (col>=n)
        if(isOutOfArrayBounds) return false
        
        val target = board[row][col]
        if(target != word[index]) return false
        if(index==word.lastIndex) return true
        
        board[row][col] = '1'
        val isLeftValid = dfs(board, row, col-1, word, index+1)
        val isRightValid = dfs(board, row, col+1, word, index+1)
        val isTopValid = dfs(board, row-1, col, word, index+1)
        val isBottomValid = dfs(board, row+1, col, word, index+1)
        board[row][col] = target
        if(isLeftValid||isRightValid||isTopValid||isBottomValid) return true
        return false
    }
}