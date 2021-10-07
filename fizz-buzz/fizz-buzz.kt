class Solution {
fun fizzBuzz(n: Int): List<String> {
    val answer: List<String> = arrayListOf<String>().apply {
        for(i in 1..n){
            if(i.rem(15)==0) add("FizzBuzz")
            else if(i.rem(3)==0) add("Fizz")
            else if(i.rem(5)==0) add("Buzz")
            else add(i.toString())
        }
    }
    return answer
}
}