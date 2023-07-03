class Solution:
            
    def digitSum(self, n: int) -> int:
        sum = 0
        # print("n: %d" % n)
        while n > 0:
            sum += (n % 10)**2
            n  = n // 10
            
        # print("sum: %d" % sum)
        return sum

    def isHappy(self, n: int) -> bool:
        digitSum = self.digitSum(n)
        k = 0
        while digitSum != 1:
            digitSum = self.digitSum(digitSum)
            if digitSum < 10 and digitSum !=1:
                return False
    
        return True
