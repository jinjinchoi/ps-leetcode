class Solution {
    fun reverseWords(s: String): String {
        
        val reversedList: List<String> = s.trim().split("\\s+".toRegex()).reversed()
        var returnStr = ""
        reversedList.dropLast(1).forEach{
            returnStr += it + " "
        }
        
        returnStr += reversedList.last()
        
        return returnStr
    }
}