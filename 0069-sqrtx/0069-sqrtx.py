class Solution:
    def mySqrt(self, x: int) -> int:
        sqrt = 0
        while sqrt**2 <= x:
            sqrt += 1
        return sqrt -1
        