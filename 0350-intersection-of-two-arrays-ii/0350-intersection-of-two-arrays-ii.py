from collections import defaultdict
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        num_hash = defaultdict(int)
        for n in nums1:
            num_hash[n] += 1
            
        for n in nums2:
            if num_hash[n]>0:
                num_hash[n] -= 1
                result.append(n)
        return result