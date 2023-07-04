from collections import defaultdict

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # num_list = [] # space complexity O(n)
        # for number in nums: # time complexity *n
        #     if number in num_list: # time complexity *n
        #         num_list.remove(number)
        #     else:
        #         num_list.append(number)
        # return num_list.pop()
        hash_table = defaultdict(int)
        for number in nums: # time complexity n
            hash_table[number] += 1
        for key in hash_table: # time complexity n
            if hash_table[key] == 1:
                return key
        