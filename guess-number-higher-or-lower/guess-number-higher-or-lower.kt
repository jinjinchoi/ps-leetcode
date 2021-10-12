/** 
 * The API guess is defined in the parent class.
 * @param  num   your guess
 * @return 	     -1 if num is lower than the guess number
 *			      1 if num is higher than the guess number
 *               otherwise return 0
 * fun guess(num:Int):Int {}
 */

class Solution:GuessGame() {
    override fun guessNumber(n:Int):Int {
        if(n==1) return 1
        return guessFromRange(1, n)
    }
    
    fun guessFromRange(low:Int, high:Int): Int{
        if(high<=low) return low
        var mid = low + (high - low + 1) / 2
        
        return when(guess(mid)){
            0 -> mid
            -1 -> guessFromRange(low, mid-1)
            1 -> guessFromRange(mid+1, high)
            else -> 0
        }
    }
}