class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_list = []
        for number in nums:
            if number in num_list:
                num_list.remove(number)
            else:
                num_list.append(number)
        return num_list.pop()