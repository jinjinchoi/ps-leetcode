class Solution {
    fun canConstruct(ransomNote: String, magazine: String): Boolean {
        var magazineHash = HashMap<Char, Int>()
        magazine.forEach{ c->
            magazineHash.put(c, magazineHash.getOrDefault(c, 0)+1)
        }
    
        ransomNote.forEach{ m->
            if (magazineHash.getOrDefault(m, 0) == 0) return@canConstruct false
            magazineHash.put(m, magazineHash.getOrDefault(m, 0)-1)
        }
        return true
    }
}