class Solution {
    fun transpose(matrix: Array<IntArray>): Array<IntArray> {
        val rowNum = matrix.size
        val columnNum = matrix[0].size
        var transposeMatrix = Array(columnNum, {IntArray(rowNum)} )
        matrix.forEachIndexed{ i, row ->
            row.forEachIndexed{ j, col ->
                transposeMatrix[j][i] = col
            }
        }
        return transposeMatrix
    }
}