from collections import defaultdict
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_hash = defaultdict(int)
        for n in nums:
            if num_hash[n]==1:
                return True 
            else:
                num_hash[n] += 1
        return False
        