class Solution {
    fun solution(numbers: IntArray): String {
        var answer = ""
        
        numbers.sortedWith(
            Comparator({ num1, num2 ->
                "$num2$num1".compareTo("$num1$num2")
            })
        ).forEach{
            answer += it.toString()
        }
        if(answer.startsWith('0')) return "0"
        return answer
    }
}
