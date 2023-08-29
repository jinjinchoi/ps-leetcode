class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_length = len(word1)
        word2_length = len(word2)
        index1 = 0
        index2 = 0
        output = ""
        while index1 < word1_length or index2 < word2_length:
            if index1 < word1_length:
                output += word1[index1]
                index1 += 1
            if index2 < word2_length:
                output += word2[index2]
                index2 += 1
        return output
            
        