class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        hashmap = {}
        max_length = 0
        cum_sum = 0
        for i, n in enumerate(nums):
            cum_sum += n
            if cum_sum == k:
                max_length = max(max_length, i+1)
            if cum_sum-k in hashmap:
                max_length = max(max_length, i-hashmap[cum_sum-k])
            if cum_sum not in hashmap:
                hashmap[cum_sum] = i
        return max_length
