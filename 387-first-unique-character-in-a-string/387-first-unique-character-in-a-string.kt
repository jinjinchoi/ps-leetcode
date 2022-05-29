class Solution {
    fun firstUniqChar(s: String): Int {
        var charHash = HashMap<Char, Int>()
        s.forEachIndexed{ i, targetChar ->
            charHash.put(targetChar, charHash.getOrPut(targetChar){0} + 1)
        }
        // var index = -1
        // for(i)
        // charHash.forEach { char, count ->
        //     if(count==1) return s.indexOf(char)
        // }
        // println("s:" + s)
        s.forEach{ char ->
            if(charHash.get(char) == 1) return s.indexOf(char)
        }
        
//         for ((char, count) in charHash) {
//             println("char: "+char+" count: "+count)
//             if(count==1) return s.indexOf(char)
//         }
        
        return -1
    }
}