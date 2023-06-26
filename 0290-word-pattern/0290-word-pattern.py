class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split()
        p_list = list(pattern)
    
        return list(map(s_list.index, s_list)) == list(map(p_list.index, p_list))
            
        
        