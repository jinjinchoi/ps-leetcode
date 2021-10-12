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
    
    fun guessFromRange(_low:Int, _high:Int): Int{
        var high = _high
        var low = _low
        var mid = low + (high - low + 1) / 2 
        println("high: $high, low: $low, mid: $mid")
        when{
            guess(mid) < 0 -> high = mid-1
            guess(mid) == 0 -> return mid
            guess(mid) > 0 -> low = mid+1
        }
        
        return guessFromRange(low, high)
    }
}