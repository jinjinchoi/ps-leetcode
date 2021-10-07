class Solution {
fun calculateMinimumHP(dungeon: Array<IntArray>): Int {
        //println("first: ${dungeon[0][0]}")
        val firstElement = dungeon[0][0]
        val m = dungeon.size
        val n = dungeon[0].size
        var sum = 0
        var sumArr = IntArray(m*n)
        //println("m: $m")
        //println("n: $n")
        
        var answer = dungeon.copyOf()
        for(i in m-1 downTo 0){
            for(j in n-1 downTo 0){
                if(i == m-1 && j == n-1) {
                    answer[i][j] = 1 + maxOf(0, - maxOf(0, answer[i][j]) - minOf(0, answer[i][j]))
                    //println("answer[$i][$j]: ${answer[i][j]}")
                }
                else if(i == m-1) {
                    answer[i][j] = maxOf(1, answer[i][j+1] - maxOf(0, answer[i][j]) - minOf(0, answer[i][j]))
                	//println("answer[$i][$j]: ${answer[i][j]}")
                }
                else if(j == n-1) {
                    answer[i][j] = maxOf(1, answer[i+1][j] - maxOf(0, answer[i][j]) - minOf(0, answer[i][j]))
                	//println("answer[$i][$j]: ${answer[i][j]}")
                }
                else {
                    answer[i][j] = maxOf(1, minOf(answer[i+1][j], answer[i][j+1]) - maxOf(0, answer[i][j]) - minOf(0, answer[i][j]))
                	//println("answer[$i][$j]: ${answer[i][j]}")
                }
            }
        }
        
        return answer[0][0]
    }
}