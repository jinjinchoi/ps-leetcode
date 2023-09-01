from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False

        counter_s = Counter(s)
        for char in t:
            counter_s[char] -= 1
            
        for key in counter_s.keys():
            if (counter_s[key]!=0):
                return False
        
        return True