class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        # nums = [4,7,9,10], k = 1
        # missing_count_array = [0, 2, 3, 3]
        
        # 0, 0, 1
        # find i from missing_count_array where i >= k for the first time
        # then return nums[i-1] + k - missing_count_array[i-1]
        missing_count_array = [nums[idx] - nums[0] - idx for idx in range(len(nums))]
        if k > missing_count_array[-1]:
            return nums[-1] + k - missing_count_array[-1]
        left, right = 0, len(nums)-1
        index = -1
        while left <= right:
            mid = (left+right)//2
            if missing_count_array[mid]>=k:
                index = mid
                right = mid - 1
            else:
                left = mid + 1
            
        return nums[index-1] + k - missing_count_array[index-1]
                
        
        