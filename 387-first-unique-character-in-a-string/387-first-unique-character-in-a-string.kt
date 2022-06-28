class Solution {
    fun firstUniqChar(s: String): Int {
        var charHash = HashMap<Char, Int>()
        s.forEachIndexed{ i, targetChar ->
            charHash.put(targetChar, charHash.getOrPut(targetChar){0} + 1)
        }
        s.forEach{ char ->
            if(charHash.get(char) == 1) return s.indexOf(char)
        }
        return -1
    }
}