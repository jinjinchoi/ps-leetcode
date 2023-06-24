from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_hash = defaultdict(int)
        for n in nums:
            count_hash[n] += 1
            
        return max(count_hash, key=count_hash.get)