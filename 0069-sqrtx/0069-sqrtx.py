class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        left, right = 2, x//2
        
        while left <= right:
            piv = (left) + (right - left) // 2
            num = piv **2
            if num > x:
                right = piv -1
            elif num < x:
                left = piv + 1
            else:
                return piv
        return right
    
        