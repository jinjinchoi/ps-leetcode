class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_stack = []
        for number in nums:
            if number in num_stack:
                num_stack.remove(number)
            else:
                num_stack.append(number)
        return num_stack.pop()