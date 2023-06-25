class Solution:
    def reverseBits(self, n: int) -> int:
        exp = 31
        result = 0
        while n>0:
            result += ( n & 1 ) << exp
            exp -= 1
            n = n>>1
        return result