class Solution:
            
    def digit_sum(self, n: int) -> int:
        sum = 0
        while n > 0:
            n, digit = divmod(n, 10)
            sum += digit **2
        return sum

    def isHappy(self, n: int) -> bool:
        seen_set = set()
        while n != 1 and n not in seen_set:
            seen_set.add(n)
            n = self.digit_sum(n)
    
        return n == 1
