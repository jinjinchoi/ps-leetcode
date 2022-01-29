class Solution {
    fun numSquares(n: Int): Int {
        val numSquareArray = IntArray(n+1)
        
        var maxSquare = 1
        
        (1..n).forEach{ i ->
            //println("numSquareArray[$i] : initial $i")
            numSquareArray[i] = i
            if(maxSquare*maxSquare == i){
                maxSquare += 1
                numSquareArray[i] = 1
                //println("numSquareArray[$i] : square(1)")
            }else{
                var minCount = i
                //println("maxSquare $maxSquare")
                (2..maxSquare-1).forEach{ square ->
                    //println("n: $n, square: $square")
                    var newCount = 1 + numSquareArray[i-square*square]
                    if(minCount > newCount) {
                        minCount = newCount 
                        //println("numSquareArray[$i] : square(1)")
                    }
                }
                numSquareArray[i] = minCount
            }
            
        }
        return numSquareArray[n]
    }
}