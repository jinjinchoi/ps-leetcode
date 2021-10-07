class Solution {
    fun islandPerimeter(grid: Array<IntArray>): Int {
        var perimeter = 0
        val maxRow = grid.count() - 1
        val maxCol = grid[0].count() - 1
    	grid.forEachIndexed{ i, row ->
            row.forEachIndexed{ j, element ->
                if(element==0) return@forEachIndexed
                if(i==0) perimeter += 1 else perimeter += (1 - grid[i-1][j])
                if(j==0) perimeter += 1 else perimeter += (1 - grid[i][j-1])
                if(i==maxRow) perimeter += 1 else perimeter += (1 - grid[i+1][j])
                if(j==maxCol) perimeter += 1 else perimeter += (1 - grid[i][j+1])
            }
        }   
        return perimeter
    }
}