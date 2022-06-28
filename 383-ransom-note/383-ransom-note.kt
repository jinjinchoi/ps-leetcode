class Solution {
    fun canConstruct(ransomNote: String, magazine: String): Boolean {
        var magazineHash = HashMap<Char, Int>()
        var value = 0
        magazine.forEach{ c->
            magazineHash.put(c, magazineHash.getOrDefault(c, 0)+1)
        }
    
        ransomNote.forEach{ m->
            value = magazineHash.getOrDefault(m, 0)
            if (value == 0) return@canConstruct false
            magazineHash.put(m, value-1)
        }
        return true
    }
}